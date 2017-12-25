from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import time
driver=webdriver.Chrome()
driver.get('https://www.facebok.com/login')   #driver.get(url)-- We get url by using driver which we initialy load.    
print ("Opened Facebook")
time.sleep(5)    #Just wait for sometime.
email = driver.find_element_by_xpath("//input[@id='email' or @name='email']") #Find email textaera.
email.send_keys('rohitpandey486@gmail.com')  #Send email to this text area. 
password = driver.find_element_by_xpath("//input[@id='pass']") #Find password textarea.
password.send_keys('**********')   #send password to the password field.
button = driver.find_element_by_xpath("//*[@id='loginbutton']")  #Find login button.
button.click()      #Click on login button.
statusbox = driver.find_element_by_xpath("//*[@name='xhpc_message']")    #Finding statusbox.
statusbox.send_keys("Bot is typing here");    #sending text to the statusbox.
postbutton = driver.find_element_by_xpath("//*[text()='Post']") #Find Postbtton.
postbutton.click()     #Press postbutton.
print ("Your status posted sucessfully")
