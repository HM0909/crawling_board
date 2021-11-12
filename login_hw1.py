from selenium import webdriver
import urllib.request as ur
from bs4 import BeautifulSoup as bs
import time
import csv
from urllib import request

# https://www.museum.go.kr/site/main/homeF

base_url = "https://www.museum.go.kr/site/main/archive/post/category/category_52"
login_url = "https://www.museum.go.kr/site/main/member/public/login?returnUrl=https%3A%2F%2Fwww.museum.go.kr%2Fsite%2Fmain%2FhomeF"

driver = webdriver.Chrome(executable_path='C:\hm_py\chromedriver')
driver.get(login_url)

user_id = ""
password = ""

# driver.find_element_by_class_name('lg_local_btn').click()
driver.find_element_by_id('id').send_keys(user_id)
time.sleep(5)
driver.find_element_by_id('pwd').send_keys(password)
time.sleep(5)
# driver.find_element_by_class_name('btn_g btn_confirm submit').click()
driver.find_element_by_xpath('//*[@id="wrap"]/div/div/div[2]/div/div[1]/div[2]/div/a').click()


time.sleep(5)

driver.get(base_url)

soup = bs(ur.urlopen(base_url).read(), 'html.parser')  #??

page_num = soup.find("div",  {"class" : "num"})
page_num_all = page_num.find("span").text

for i in range(1, int(page_num_all)) :  
    if  i <= 2 :
        if i > 1:
            driver.get(base_url + "?catId=52&cp=" + str(i))
            soup = bs(ur.urlopen(base_url).read(), 'html.parser')  #??
            page_num = soup.find("div",  {"class" : "num"})
            page_num_all = page_num.find("span").text
        
        root = soup.find("div", {"class":"board-list-tbody"})
        items = root.find_all("ul")

        for item in items:
            data = item.find("li", {"class":"l"})
            link = data.find("a")
            link_url = link.get("href")
            
            driver.get( 'https://www.museum.go.kr' + link_url)

            detail_html = driver.page_source 
            detail_soup = bs(detail_html, 'html.parser')

            title = detail_soup.find("strong", {"class" : "subject"})
            section = detail_soup.find("div", {"class" : "pointColor04"})
            author = detail_soup.find("ul", {"class" : "view-l"})
            post = author.find_all("li")

            file_info = detail_soup.find("li", {"class" : "file"})
            file_url = file_info.find("a").get("href")
            file_name = file_info.find("a").text
            
            print(title.text)
            print(section.text)
            print(post[0].text.replace("등록일", "").strip())
            print(post[1].text.replace("조회수", "").strip())
            print(file_url)
            print(file_name)
            
            ext = ".pdf"
            pos = file_name.find(ext)

            url = "https://www.museum.go.kr" + file_url 
            savename = "c:/hm_py/crawling/" + file_name[:pos]+ext
            request.urlretrieve(url, savename)
