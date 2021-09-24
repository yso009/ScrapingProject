from selenium import webdriver
from bs4 import BeautifulSoup as BS
from urllib.request import urlretrieve #다운로드
from urllib.parse import quote_plus

def img_scraping(keyword, count, path):
    url = "https://www.google.com/search?q=" + str(keyword) + "&hl=ko&tbm=isch" # 구글 이미지창 주소
    
    browser=webdriver.Chrome()
    browser.get(url)

    html = browser.page_source
    soup = BS(html,features="html.parser")

    img = soup.select('img')

    i_list =[]
    cnt = 1

    for i in img:
        try:
            i_list.append(i.attrs["src"])
        except KeyError:
            i_list.append(i.attrs["data-src"])
    
    for i in i_list:
        urlretrieve(i,"C:\\Users\\user\\Desktop\\이재용\\"+keyword+str(cnt)+".jpg")
        cnt += 1
        if cnt == count:
            break
    browser.close()
    print(str(cnt)+"개 다운로드")

img_scraping("이재용",15,'')
