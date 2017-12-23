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
import os
driver=webdriver.Chrome()
driver.get('https://www.twitter.com/login')   #driver.get(url)-- We get url by using driver which we initialy load.    
print ("Opened Twitter")
time.sleep(5)    #Just wait for sometime.
email = driver.find_element_by_xpath("//*[@class='js-username-field email-input js-initial-focus']")  #Find email textaera.
email.send_keys('rohitpandey486@gmail.com')       #Send email to this text area.
password = driver.find_element_by_xpath("//*[@class='js-password-field']")  #Find password textarea.
password.send_keys('********')      #send password to the password field.
button = driver.find_element_by_xpath("//*[@class='submit EdgeButton EdgeButton--primary EdgeButtom--medium']")  #Find login button.
button.click()        #Click on login button.
statusbox=driver.find_element_by_xpath("//div[@id='tweet-box-home-timeline']")    #Finding statusbox.
statusbox.send_keys("Bot is typing here")     #sending text to the statusbox.
tweetbutton = driver.find_element_by_xpath("//*[@class='tweet-action EdgeButton EdgeButton--primary js-tweet-btn']") #Find tweetbtton.
postphoto=driver.find_element_by_xpath("//*[@type='file']")
postphoto.send_keys('/home/pandey-ubuntu/photos/hello.png')
tweetbutton.click()     #Press tweetbutton.
print ("Your status and photo posted sucessfully")
