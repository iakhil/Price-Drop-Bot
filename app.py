from ast import parse
from bs4 import BeautifulSoup
from flask import Flask, request
from flask import Response
import requests  
import telegram
import time 
import os 
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

url = "https://www.flipkart.com/microsoft-xbox-series-s-512-gb/p/itm13c51f9047da8?pid=GMCFVPFCNHHZQBNA&lid=LSTGMCFVPFCNHHZQBNAH1ZPTY&marketplace=FLIPKART&q=xbox+series+s&store=4rr%2Fx1m&spotlightTagId=BestsellerId_4rr%2Fx1m&srno=s_1_2&otracker=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&fm=search-autosuggest&iid=e08f4ae5-d092-4382-8940-b5333bcec7b2.GMCFVPFCNHHZQBNA.SEARCH&ppt=sp&ppn=sp&ssid=n0c2wnrw8w0000001666680069962&qH=87582353119ece1a"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")


TOKEN=os.getenv('API_KEY')
bot = telegram.Bot(token=TOKEN)
chat_id = os.getenv('CHAT_ID')


def get_price():

    mydivs = soup.find("div", {"class": "_30jeq3 _16Jk6d"})
    price = (mydivs.text).replace(',', '')[1:]
    return int(price)


@app.route('/', methods=['GET','POST'])
def index():
    msg = request.get_json()
    while (1):
        price = get_price()
        if int(price) <= 29990:
            result = time.gmtime(time.time())
            bot.sendMessage(chat_id=chat_id, text="No sale. Current price: " + str(price)) 
        else:
            result = time.gmtime(time.time())
            if (result.tm_min == 0 or result.tm_min == 30):
                bot.sendMessage(chat_id=chat_id, text="There is a sale! Curent price: " + str(price))

    return Response('ok', status=200)

 
if __name__ == '__main__':

    app.run(debug=True)
