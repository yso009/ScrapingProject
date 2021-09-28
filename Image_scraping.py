from selenium import webdriver
from bs4 import BeautifulSoup as BS
from urllib.request import urlretrieve #다운로드
from urllib.parse import quote_plus
import os

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
        try:
            if not os.path.exists("C:\\Users\\user\\Desktop\\image\\"+keyword): # Keyword 폴더가 존재하지 않는다면
                os.makedirs("C:\\Users\\user\\Desktop\\image\\"+keyword)  # 폴더 생성
        except:
            continue
        urlretrieve(i,"C:\\Users\\user\\Desktop\\image\\"+keyword+"\\"+keyword+str(cnt)+".jpg")
        cnt += 1
        if cnt == (count+1):
            break
    browser.close()
    os.startfile("C:\\Users\\user\\Desktop\\image\\"+keyword) #폴더 열기
    print(str(count)+"개 다운로드")

img_scraping(input("이름 : "),int(input("장수 : ")))

