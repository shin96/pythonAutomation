from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import datetime


def sendthis(msg, target, delay, wait, times=1):
    # select the contact from the side bar
    contact_path = '//*[@id="side"]/div[2]/div/label/input'
    # wait till the contact is visible on the side bar
    search_contact_name = wait.until(ec.presence_of_element_located((By.XPATH, contact_path)))
    search_contact_name.send_keys(target + Keys.ENTER)
    # paste ur msg to send
    inputbox_path = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
    enter_msg_and_send = wait.until(ec.presence_of_element_located((By.XPATH, inputbox_path)))
    # enter_msg_and_send.send_keys(msg, Keys.ENTER)
    time.sleep(delay)
    for i in range(times):
        enter_msg_and_send.send_keys(msg, Keys.ENTER)
        # time.sleep(1)
    print("msg is successfully sent!! now closing chrome")
    time.sleep(1)
    browser.close()

browser = webdriver.Chrome()
browser.get("https://web.whatsapp.com/")
wait = WebDriverWait(browser, 500)
target = input('enter the name of the contact: ')
msg = input("enter your msg: ")
print("after how many hour : min: sec u want to send your msg ?")
print("ex: 0:0:5 this will send ur msg after 5 sec)")
your_time = input().split(':')
your_time = [int(i) for i in your_time]
time_now = datetime.datetime.now()
send_at = time_now + datetime.timedelta(hours=your_time[0], minutes=your_time[1], seconds=your_time[2])
delay = (send_at - time_now).total_seconds()

print("the msg will be sent at", send_at)
sendthis(msg, target, delay, wait)

