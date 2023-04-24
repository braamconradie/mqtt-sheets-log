#need to pip install 
# pip3 install -r requirements.txt 

# check stuff is working
# gc = gspread.service_account(filename='credentials.json')
# sh = gc.open_by_key('1B0plp_7tp5cXrN1ce1JcFG5e9RnLjBSJ-cIeUGS_rcE')
# worksheet = sh.sheet1 
# res = worksheet.get_all_records()
# print(res)


# get the spreadsheet
import gspread
import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

broker = 'broker.emqx.io'

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    #client.subscribe(sub_topic)

def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

def on_message(client, userdata, msg):
    message = str(msg.payload)
    print(msg.topic+" "+message)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, 1883, 60)
client.loop()

for i in range(5):
    client.publish("vscode", "alive")