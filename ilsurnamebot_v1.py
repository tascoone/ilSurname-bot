import telebot
import requests
import random
import time
import requests


API_KEY = "<API KEY>"
bot = telebot.TeleBot(API_KEY)
comandi = "/help : mostra i comandi"\
    "\n/rickroll : rickrolla chiunque"\
    "\n/btceuro : mostra il prezzo dei bitcoin"
    "\n/insulta + username : indovina cosa fa 😎😎"


@bot.message_handler(commands=["help"])
def help(message):
    bot.reply_to(message, comandi )

@bot.message_handler(commands=["rickroll"])
def rickroll(message):
  bot.send_message(message.chat.id,"https://youtu.be/dQw4w9WgXcQ")

@bot.message_handler(commands=["btceuro"])
def btc_to_euro(message):
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    bitcoin_prices = r.json()
    bot.reply_to(message, "I bitcoin ora costano: " + bitcoin_prices["bpi"]["EUR"]["rate"] + " , ma tanto sei povero come la merda...")

@bot.message_handler(commands=["insulta"])     
def insulta(message):
    insulti = ["sei un coglione",
    "fai schifo a livello molecolare", 
    "se ti schiaffeggio porti fortuna come la merda", 
    "quando tua mamma ti ha visto ha detto \"è proprio uscito dal culo\""]
    username = message.text[8:]
    bot.send_message(message.chat.id, username + " " + random.choice(insulti))


bot.polling()
