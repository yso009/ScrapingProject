from selenium import webdriver
from bs4 import BeautifulSoup as BS
from urllib.request import urlretrieve #다운로드
from urllib.parse import quote_plus

def img_scraping(keyword, count):
    url = "https://www.google.com/search?q=" + str(keyword) + "&hl=ko&tbm=isch" # 구글 이미지창 주소
    
    browser=webdriver.Chrome()
    browser.get(url)

    html = browser.page_source
    soup = BS(html,features="html.parser")

    img = soup.select('div.bRMDJf > img') # Class = bRMDJF 가 들어있는 div 하위에 img 지정

    img_list =[]
    cnt = 1

    for i in img:
        try:
            img_list.append(i.attrs["src"])
        except KeyError:
            img_list.append(i.attrs["data-src"])
    
    for i in img_list:
        urlretrieve(i,"C:\\Users\\user\\Desktop\\"+keyword+"\\"+keyword+str(cnt)+".jpg")
        cnt += 1
        if cnt == count:
            break
    browser.close()
    print(str(cnt)+"개 다운로드")

img_scraping(input("이름 : "),int(input("장수 : ")))

