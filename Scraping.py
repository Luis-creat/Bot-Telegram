import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import telebot

Service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service, options=options)

url = 'https://www.revistaduasrodas.com.br/noticias'
driver.get(url)

noticias = []
lista_text = []
lista_link = []

for i in range(10):
    print(driver.find_elements(By.CLASS_NAME, 'i-noticias')[i].text)
    print(driver.find_elements(By.CLASS_NAME, 'i-noticias')[i].find_element(By.TAG_NAME, 'a').get_attribute("href"))
    print()

    text = driver.find_elements(By.CLASS_NAME, 'i-noticias')[i].text
    link = driver.find_elements(By.CLASS_NAME, 'i-noticias')[i].find_element(By.TAG_NAME, 'a').get_attribute("href")

    lista_text.append(text)
    lista_link.append(link)

    
print(lista_text)
