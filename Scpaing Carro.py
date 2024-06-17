import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')  # Executar em modo headless (sem abrir a janela do navegador)
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)

url = 'https://quatrorodas.abril.com.br/ultimas-noticias/'
driver.get(url)

noticias = []
lista_text = []
lista_link = []

for i in range(10):
    print(driver.find_elements(By.CSS_SELECTOR, 'div.card.not-loaded.list-item')[i].text)
    print(driver.find_elements(By.CSS_SELECTOR, 'div.card.not-loaded.list-item')[i].find_element(By.TAG_NAME, 'a').get_attribute("href"))
    print()