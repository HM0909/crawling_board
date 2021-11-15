from selenium import webdriver
import urllib.request as ur
from bs4 import BeautifulSoup as bs
import time
import csv
from urllib import request

# https://www.museum.go.kr/site/main/homeF

base_url = "https://www.museum.go.kr/site/main/archive/post/category/category_52"
# page_url = base_url + "?cp=i&catId=52"

driver = webdriver.Chrome(executable_path='C:\hm_py\chromedriver')   
    
driver.get(base_url)

soup = bs(ur.urlopen(base_url).read(), 'html.parser')
page_num = soup.find("div",  {"class" : "num"})
page_num_all = page_num.find("span").text
page_num_now = page_num.find("strong").text

print(page_num_all)
print(page_num_now)

i= page_num_now

for i in range(1, int(page_num_all)) :   
    if  i <= 2 :
        print(base_url + "?catId=52&cp=" + str(i))
        driver.get(base_url + "?catId=52&cp=" + str(i))
        # print(driver.get(base_url + "?cp=" + "page_num_now" + "&catId=52"))