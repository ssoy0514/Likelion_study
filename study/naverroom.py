from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #selenium에서 사용할 모듈 import

import time
import requests
from bs4 import BeautifulSoup
import re
import csv
driver = webdriver.Chrome("./chromedriver.exe") #selenium 사용에 필요한 chromedriver.exe 파일 경로 지정

driver.get("https://map.naver.com/v5/?c=14138086.5321113,4521084.3550941,13,0,0,0,dh") #네이버 신 지도 

search_box = driver.find_element_by_class_name("input_search")
search_box.send_keys("안암 원룸")
search_box.send_keys(Keys.ENTER)
time.sleep(3)

frame = driver.find_element_by_css_selector("iframe#searchIframe")

driver.switch_to.frame(frame)
time.sleep(2)

# 여기까지 iframe 전환

scroll_div = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]")
#검색 결과로 나타나는 scroll-bar 포함한 div 잡고
driver.execute_script("arguments[0].scrollBy(0,2000)", scroll_div)
time.sleep(1)
driver.execute_script("arguments[0].scrollBy(0,2000);", scroll_div)
time.sleep(1)
driver.execute_script("arguments[0].scrollBy(0,2000);", scroll_div)
time.sleep(1)
driver.execute_script("arguments[0].scrollBy(0,2000);", scroll_div)
time.sleep(1)
driver.execute_script("arguments[0].scrollBy(0,2000);", scroll_div)
time.sleep(1)
#여기까지 scroll
#맨 아래까지 내려서 해당 페이지의 내용이 다 표시되게 함

# csv 파일 생성
file = open('naverroom.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["name","address"])
final_result = []
time.sleep(1)
# # 반복 시작
i=1
while i<=6
 #몇 페이지까지 크롤링할 것인지 지정
   rooms_box = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/ul")
   rooms = rooms_box.find_elements_by_css_selector("li._22p-O._2NEjP")
   #해당 페이지에서 표시된 모든 가게 정보
   
   for room in rooms: #한 페이지 내에서의 반복문. 순차적으로 가게 정보에 접근
       name = room.find_element_by_css_selector("span._3Apve").text #가게 이름
       time.sleep(2)
       click_name = room.find_element_by_css_selector("span._3Apve")
       click_name.click() 
       # 가게 주소, 홈페이지 링크를 확인하려면 가게 이름을 클릭해 세부 정보를 띄워야 함.
        
    


       driver.switch_to.default_content()
       time.sleep(2)     
       ##오래 헤맸던 부분!! switch_to.default_content()로 전환해야 frame_in iframe을 제대로 잡을 수 있다. 
       
       frame_in = driver.find_element_by_xpath('/html/body/app/layout/div[3]/div[2]/shrinkable-layout/div/app-base/search-layout/div[2]/entry-layout/entry-place-bridge/div/nm-external-frame-bridge/nm-iframe/iframe')

       driver.switch_to.frame(frame_in) 
       # 가게 이름을 클릭하면 나오는 세부 정보 iframe으로 이동
       time.sleep(2)
       try:
           address = driver.find_element_by_css_selector("span._2yqUQ").text
       except:
           address = ''
          #주소 정보 확인

       room_info = {
           'name':name,
            'address':address
           }

       #크롤링한 정보들을 store_info에 담고
       print(name, address)
       print("*" * 50)
       final_result.append(room_info)
       # 출력해서 확인 후 final_result에 저장

       driver.switch_to.default_content()
       driver.switch_to.frame(frame)
       time.sleep(1)
       # 한 페이지 크롤링 끝
    
    next_button = driver.find_element_by_css_selector("svg._2bgjk")
    next_button.click()
    si = i+1
   time.sleep(2)


for result in final_result: #크롤링한 가게 정보에 순차적으로 접근 & csv 파일 작성
    row = []
    row.append(result['name'])
    row.append(result['address'])
    writer.writerow(row)
    
print(final_result)
#최종 결과 확인