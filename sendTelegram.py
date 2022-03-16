import sys
import os
import telegram
import json
import datetime

argvs = sys.argv
message = argvs[1]

iDir = os.path.abspath(os.path.dirname(__file__))

with open(iDir + '/config.json') as fc:
    conf = json.load(fc)

with open(iDir + '/message.json') as fm:
    mes = json.load(fm)

bot = telegram.Bot(token=conf["TOKEN"])
dt_now = datetime.datetime.now()
try:
    bot.send_message(chat_id=conf["CHAT_ID"], text=mes[message])
    print('%s [OK] : %s ' %(dt_now, mes[message]))
except:
    print('%s [Error]' %dt_now)