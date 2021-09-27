from selenium import webdriver
from bs4 import BeautifulSoup as soups

def search_selenium(search_name, search_path, search_limit) :
    search_url = "https://www.google.com/search?q=" + str(search_name) + "&hl=ko&tbm=isch" # 구글 이미지창 주소 
    
    browser = webdriver.Chrome() 
    browser.get(search_url) # 이미지 창 띄우기
    
    browser.implicitly_wait(2)

    images = browser.find_elements_by_class_name("rg_i")
    cnt = 0

    for image in images:
        image.get_attribute("img")
        image.screenshot("C:\\Users\\user\\Desktop\\이재용\\" + str(cnt) + ".jpg")
        cnt += 1
        if cnt == search_limit:
            break
    print("저장한 이미지 수 : " , cnt)
    browser.close()

if __name__ == "__main__" :

    search_name = input("검색하고 싶은 키워드 : ")
    search_limit = int(input("원하는 이미지 수집 개수 : "))
    search_path = "C:\\Users\\user\\Desktop\\이재용"
    search_selenium(search_name, search_path, search_limit)