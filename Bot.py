import telebot
from telebot import types
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import time

# Token do bot
token = '7135262689:AAGQvN1P1m3HoW0aWsxW3DQY7Xk2_3hwXNU'
bot = telebot.TeleBot(token)

#Cinguração do webdriver
chrome_options = Options()
chrome_options.add_argument('--headless')  # Executar em modo headless (sem abrir a janela do navegador)
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Configuração do webdriver para acessar as notícias de motos e carros
driver_moto = webdriver.Chrome(options=chrome_options)
url_moto = 'https://www.revistaduasrodas.com.br/noticias'
driver_moto.get(url_moto)

driver_carro = webdriver.Chrome(options=chrome_options)
url_carro = 'https://quatrorodas.abril.com.br/ultimas-noticias/'
driver_carro.get(url_carro)

# Listas para armazenar as notícias
lista_text_moto = []
lista_link_moto = []
lista_text_carro = []
lista_link_carro = []
#loop para pegar as notícias
for i in range(10):
    print(driver_moto.find_elements(By.CLASS_NAME, 'i-noticias')[i].text)
    print(driver_moto.find_elements(By.CLASS_NAME, 'i-noticias')[i].find_element(By.TAG_NAME, 'a').get_attribute("href"))
    print()

    print(driver_carro.find_elements(By.CSS_SELECTOR, 'div.card.not-loaded.list-item')[i].text)
    print(driver_carro.find_elements(By.CSS_SELECTOR, 'div.card.not-loaded.list-item')[i].find_element(By.TAG_NAME, 'a').get_attribute("href"))
    print()

    text_moto = driver_moto.find_elements(By.CLASS_NAME, 'i-noticias')[i].text
    link_moto = driver_moto.find_elements(By.CLASS_NAME, 'i-noticias')[i].find_element(By.TAG_NAME, 'a').get_attribute("href")

    text_carro = driver_carro.find_elements(By.CSS_SELECTOR, 'div.card.not-loaded.list-item')[i].text
    link_carro = driver_carro.find_elements(By.CSS_SELECTOR, 'div.card.not-loaded.list-item')[i].find_element(By.TAG_NAME, 'a').get_attribute("href")

    lista_text_moto.append(text_moto)
    lista_link_moto.append(link_moto)

    lista_text_carro.append(text_carro)
    lista_link_carro.append(link_carro)
#fechando os drivers
driver_moto.quit()
driver_carro.quit()

# Função para enviar mensagem e mostrar as notícias
@bot.message_handler(commands=['start'])
def enviarOI(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    moto = types.InlineKeyboardButton('Motos', callback_data='moto')
    carro = types.InlineKeyboardButton('Carros', callback_data='carro')
    markup.add(moto, carro)
    bot.send_message(message.chat.id, "Gostaria de receber noticias de qual automóvel?", reply_markup=markup)

# Função para mostrar as notícias de acordo com a opção escolhida
@bot.callback_query_handler(func=lambda call:True)
def answer(callback):
    if callback.data == 'moto':
        bot.send_message(callback.message.chat.id, "Aqui estão as últimas notícias sobre motos: ")
        for i in range(10):
            bot.send_message(callback.message.chat.id, lista_text_moto[i])
            bot.send_message(callback.message.chat.id, "Para mais informações: ")
            bot.send_message(callback.message.chat.id, lista_link_moto[i])
            bot.send_message(callback.message.chat.id, "-----------------------------------------")
        bot.send_message(callback.message.chat.id, "Caso queira mais informções, digite /noticias")
    elif callback.data == 'carro':
        bot.send_message(callback.message.chat.id, "Aqui estão as últimas notícias sobre carros: ")
        for i in range(10):
            bot.send_message(callback.message.chat.id, lista_text_carro[i])
            bot.send_message(callback.message.chat.id, "Para mais informações: ")
            bot.send_message(callback.message.chat.id, lista_link_carro[i])
            bot.send_message(callback.message.chat.id, "-----------------------------------------")
        bot.send_message(callback.message.chat.id, "Caso queira mais informções, digite /noticias")

bot.infinity_polling()