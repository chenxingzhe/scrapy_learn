from bs4 import BeautifulSoup
import requests
import time

def housescrapy(url, data=None):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    titles = soup.select('div.pho_info > h4 > em')
    addresses = soup.select('div.pho_info > p > span.pr5')
    prices = soup.select('div.day_l > span')
    img_houses = soup.select('img[id="curBigImage"]')
    img_hosts = soup.select('div.member_pic > a > img')
    sexes = soup.select('div.member_pic > div')
    #host_gender = soup.select('div.member_pic > div')[0].get('class')[0]
    for title, address, price, img_house, img_host, sex in zip(titles, addresses, prices, img_houses, img_hosts, sexes):
        if str(sex.get('class')) == "['member_ico1']":
            sex = 'female'
        else:
            sex = 'male'

        data = {
            'title': title.get_text(),
            'address': address.get_text().strip(),
            'price': price.get_text(),
            'img_house': img_house.get('src'),
            'img_host': img_host.get('src'),
            'sex': sex

        }
        print(data)
urls = ['http://hz.xiaozhu.com/search-duanzufang-p{}-0/?startDate=2016-03-01&endDate=2016-03-07'.format(str(i))
        for i in range(1,6)]
'''
#page_list > ul > li:nth-child(1) > a
'''
urls2=[]
for url in urls:

    wb_data = requests.get(url)
    #time.sleep(1)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    urls2.extend(soup.select('ul > li > a[target="_blank"]'))
    print(urls2)


for url in urls2:
    url=url.get('href')
    print(url)
    housescrapy(url)
