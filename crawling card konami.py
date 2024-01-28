import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.maximize_window()
option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-logging'])
driver.get('https://www.db.yugioh-card.com/yugiohdb/card_search.action?ope=1&sess=2&sort=21&page=1&stype=1&link_m=2&othercon=2&rp=100&page=1')

scroll_height = 300  # Scroll height in pixels
scroll_pause_time = 0.5 

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')