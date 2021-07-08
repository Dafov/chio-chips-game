import time
from selenium import webdriver

browser = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')

url = 'https://www.chio.bg/campaigns/2/party-trippin'
browser.get(url)

USERNAME_EMAIL = # Type your email here
PASSWORD = # Type your password here

time.sleep(2)
menu_btn = browser.find_element_by_xpath('//*[@id="site-header"]/div')
menu_btn.click()

time.sleep(1.5)
login_btn = browser.find_element_by_xpath('//*[@id="menu-main-menu"]/li[1]/a')
login_btn.click()

time.sleep(1.5)
username_el = browser.find_element_by_name("_email")
username_el.send_keys(USERNAME_EMAIL)

password_el = browser.find_element_by_name("_password")
password_el.send_keys(PASSWORD)

time.sleep(1.5)
submit_btn_el = browser.find_element_by_xpath("/html/body/div[2]/section/div/div[2]/div/div/form/div/div[6]/div[1]/button")
submit_btn_el.click()

time.sleep(1.5)
play_btn = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div/a/img")
play_btn.click()

time.sleep(4)
start_btn = browser.find_element_by_xpath('//*[@id="carBtnStart"]/img')
start_btn.click()