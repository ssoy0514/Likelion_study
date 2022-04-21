from numpy import rint
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

#Selenium_webdriver 위치 지정
driver = webdriver.Chrome('./chromedriver.exe')
#Selenium_driver로 url 접속
naver_url = "https://map.naver.com/v5/?c=14138086.5321113,4521084.3550941,13,0,0,0,dh"
driver.get(naver_url)
#Selenium 접속하는데 시간 걸릴 수 있으니 기다리는 시간 2초 - 의도적으로 쉬어줘야 정상적으로 결과 출력
time.sleep(3)


search_box = driver.find_element(By.CLASS_NAME, "input_search")
search_box.send_keys("안암 원룸")
search_box.send_keys(Keys.ENTER) #검색창에 "안암 원룸" 입력

time.sleep(1) #화면 표시 기다리기

frame = driver.find_element(By.CSS_SELECTOR, "iframe#searchIframe")
driver.switch_to.frame(frame)
time.sleep(1)
# 여기까지 iframe 전환


# csv 파일 생성
file = open('room.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["name", "address"])
final_result = []
time.sleep(1)

#정보 가져오는 반복문
for i in range(7):
   
   rooms_box =driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/ul")
   rooms = driver.find_elements_by_css_selector("li._22p-O._2NEjP")
   print(len(rooms))
   #해당 페이지에서 표시된 모든 건물 정보
   time.sleep(2)

   for room in rooms:
      name = room.find_element_by_css_selector("span._3Apve").text
      click_address = room.find_element_by_css_selector("svg._3NEMz")
      click_address.click()
      address = room.find_element_by_css_selector("div._2b9ic").text

      room_info = {
         'name':name,
         'address':address,
       }
      print(room_info)
      final_result.append(room_info)
   
      
   next_btn = driver.find_element_by_css_selector("svg._3D14U")
   next_btn.click()

   time.sleep(5)   

for result in final_result: #크롤링한 정보에 순차적으로 접근 , csv 파일 작성
    row = []
    row.append(result['name'])
    row.append(result['address'])
    writer.writerow(row)




print(final_result)






   next_button = driver.find_element_by_css_selector("svg._2bgjk")
   next_button.click()
   i = i+1
   time.sleep(2)