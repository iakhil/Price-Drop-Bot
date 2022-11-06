#from ast import parse
from bs4 import BeautifulSoup
from flask import Flask, request
from flask import Response
import requests  
import telegram
import time 

app = Flask(__name__)

url = "https://www.flipkart.com/microsoft-xbox-series-s-512-gb/p/itm13c51f9047da8?pid=GMCFVPFCNHHZQBNA&lid=LSTGMCFVPFCNHHZQBNAH1ZPTY&marketplace=FLIPKART&q=xbox+series+s&store=4rr%2Fx1m&spotlightTagId=BestsellerId_4rr%2Fx1m&srno=s_1_2&otracker=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&fm=search-autosuggest&iid=e08f4ae5-d092-4382-8940-b5333bcec7b2.GMCFVPFCNHHZQBNA.SEARCH&ppt=sp&ppn=sp&ssid=n0c2wnrw8w0000001666680069962&qH=87582353119ece1a"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")


TOKEN="5675588558:AAHK_G-NWD0l8fmUc2Em9o0dFPjtkxGwG20"
#print(soup.title)
def get_price():

    mydivs = soup.find("div", {"class": "_30jeq3 _16Jk6d"})
    price = (mydivs.text).replace(',', '')[1:]
   # print(int(price))
    return int(price)

def parse_message(message):
    #print("message-->", message)
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']
    return chat_id, txt 


def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot5675588558:AAHK_G-NWD0l8fmUc2Em9o0dFPjtkxGwG20/sendMessage'
    payload = {
        'chat_id': chat_id, 
        'text': text 
    }
    r = requests.post(url, json=payload)
    return r 
bot = telegram.Bot(token=TOKEN)
@app.route('/', methods=['POST', 'GET'])
def index():
    print("Entered index")
    
    #while True:
      #  msg = request.get_json()
        #print(msg)
       # chat_id, txt = parse_message(msg)
       # print("Chat ID", chat_id)
    if request.method == 'POST' or request.method == 'GET':
        msg = request.get_json()
        print(msg)
       # chat_id, txt = parse_message(msg)
        price = get_price()
        if int(price) <= 29990:
            msg = "Sale. Current price is: " + str(price) 
            bot.sendMessage(765691937, text=msg)
          #  print(chat_id, msg)
            #tel_send_message(chat_id, "No sale. Current price: " + str(price)) 
            
        else:
            price = get_price()
            msg = "No sale. Current price is: " + str(price) 
            bot.sendMessage(765691937, text=msg)
            #tel_send_message(chat_id, "There is a sale! Curent price: " + str(price))

        return Response('ok', status=200)

    else:
        print("Entered GET")
        return "<h1>Welcome!</h1>"

    # else:
    #     return "<h1>Welcome! </h1>"

bot = telegram.Bot(token=TOKEN) 
def custom_send():
    price = get_price()
    result = time.gmtime(time.time())    
    if price >= 29990:
        msg = "No sale. Current price is: " + str(price) 
        bot.sendMessage(765691937, text=msg)
        print(msg)
    else:
        msg = "Sale! Current price is: " + str(price) 
        bot.sendMessage(765691937, text=msg)
        print(msg)
    if result.tm_min == 0 or result.tm_min == 30:
        if result.tm_sec <= 5:
            bot.sendMessage(chat_id=765691937, text=msg)

if __name__ == '__main__':
    
    app.run(debug=True)
    # #print("After")
    # while (1):
    #     custom_send()
 


#https://api.telegram.org/bot5675588558:AAHK_G-NWD0l8fmUc2Em9o0dFPjtkxGwG20/setWebhook?url=https://689b-122-161-48-47.in.ngrok.io



# https://05a7-122-161-48-122.in.ngrok.io 
