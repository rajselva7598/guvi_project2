import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import csv
from csv import writer

driver = webdriver.Chrome(executable_path=r"C:\Users\user\Downloads\chromedriver_win32\chromedriver.exe")
class Create_Open:
    def get_laptops(self):
        driver.maximize_window()
        driver.get('https://www.flipkart.com')
        time.sleep(3)
        move_to_mainpage = driver.find_element(by=By.XPATH,value='/html/body/div[2]/div/div/button').click()
        time.sleep(3)
        search_input = driver.find_element(by=By.XPATH,value='//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
        search_input.send_keys("laptops")
        time.sleep(3)
        search_btn = driver.find_element(by=By.XPATH,value='//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
        search_btn.click()
        time.sleep(3)
        input_Corelist = driver.find_element(by=By.XPATH,value='//*[@id="container"]/div/div[3]/div[1]/div[1]/div/div[1]/div/section[4]/div[2]/div[1]/div[1]/input').send_keys("Core i5")
        input_Search=driver.find_element(by=By.XPATH,
                                         value='//*[@id="container"]/div/div[3]/div[1]/div[1]/div/div[1]/div/section[4]/div[2]/div[1]/div[2]/div/label/div[2]').click()
        time.sleep(3)
        hardisk_List = driver.find_element(by=By.XPATH,value='//*[@id="container"]/div/div[3]/div/div[1]/div/div[1]/div/section[10]/div').click()
        time.sleep(3)
        hardisk_capacity_Type =driver.find_element(by=By.XPATH,value='//*[@id="container"]/div/div[3]/div/div[1]/div/div[1]/div/section[10]/div[2]/div/div[1]/div/label/div[2]').click()
        time.sleep(5)
        ram_List = driver.find_element(by=By.XPATH,
                                       value='//*[@id="container"]/div/div[3]/div/div[1]/div/div[1]/div/section[18]/div').click()
        time.sleep(5)
        ram_Type = driver.find_element(by=By.XPATH,
                                       value='//*[@id="container"]/div/div[3]/div/div[1]/div/div[1]/div/section[18]/div[2]/div/div[3]/div/label/div[2]')
        time.sleep(5)
        ram_Type.click()
        time.sleep(3)
        data=requests.get(driver.current_url)
        time.sleep(3)
        soup = BeautifulSoup(data.content,'lxml')
        print(soup.text)
        name= soup.find('div', class_='col col-7-12')


        with open('new.csv','w', encoding='utf8',newline="") as f:
            thewriter = writer(f)
            thewriter.writerow(['Brand Name' , 'Price_of_the_Component'])
            for data in soup.findAll('div', class_='_3pLy-c row'):
                 names = data.find('div', class_='_4rR01T').text.replace('\n', '')
                 price = data.find('div', class_='_30jeq3 _1_WHN1').text.replace('\n', '')
                 info = [names,price]
                 thewriter.writerow(info)



        print("########################################################")

    def find_phone(self):
        driver.get('https://www.flipkart.com')
        time.sleep(3)
        search_input = driver.find_element(by=By.XPATH,value='//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
        time.sleep(3)
        search_input.send_keys("phones")
        time.sleep(3)
        search_btn = driver.find_element(by=By.XPATH,
                                         value='//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
        time.sleep(3)
        search_btn.click()
        time.sleep(3)
        ram_Search = driver.find_element(by=By.XPATH,
                                           value='//*[@id="container"]/div/div[3]/div[1]/div[1]/div/div[1]/div/section[7]/div[2]/div/div[5]/div/label/div[2]').click()
        time.sleep(3)
        hardisk_List = driver.find_element(by=By.XPATH,
                                           value='//*[@id="container"]/div/div[3]/div[1]/div[1]/div/div[1]/div/section[8]/div').click()
        time.sleep(3)
        hardisk_capacity_Type = driver.find_element(by=By.XPATH,
                                                    value='//*[@id="container"]/div/div[3]/div[1]/div[1]/div/div[1]/div/section[8]/div[2]/div/div[2]/div/label/div[2]').click()
        time.sleep(3)
        network_List = driver.find_element(by=By.XPATH,
                                       value='//*[@id="container"]/div/div[3]/div[1]/div[1]/div/div[1]/div/section[17]/div[1]').click()
        time.sleep(3)
        ram_Type = driver.find_element(by=By.XPATH,
                                       value='//*[@id="container"]/div/div[3]/div[1]/div[1]/div/div[1]/div/section[17]/div[2]/div/div[3]/div/label/div[2]').click()

        data = requests.get(driver.current_url)
        time.sleep(3)
        soup = BeautifulSoup(data.content, 'lxml')
        name = soup.find('div', class_='col col-7-12')



        with open('phone.csv','w', encoding='utf8',newline="") as f:
            thewriter = writer(f)
            thewriter.writerow(['Brand Name' , 'Price_of_the_Component'])
            for data in soup.findAll('div', class_='_3pLy-c row'):
                 names = data.find('div', class_='_4rR01T').text.replace('\n', '')
                 price = data.find('div', class_='_30jeq3 _1_WHN1').text.replace('\n', '')
                 info = [names,price]
                 thewriter.writerow(info)





createURL = Create_Open()

createURL.get_laptops()

