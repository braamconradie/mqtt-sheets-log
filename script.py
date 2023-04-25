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
import json
import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

broker = 'broker.emqx.io'

sub_topic = "stat/mospow2/STATUS10"
sub_topic2 = "werkdit"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(sub_topic)
    client.subscribe(sub_topic2)
    print("subscribed to ..." + sub_topic)

def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

# def on_message(client, userdata, msg):
#     message = str(msg.payload)
#     jsonmsg = json.loads(message)
#     print (type(jsonmsg))
#     #print(msg.topic+" "+message)

def on_message(client, userdata, msg):
    topic=msg.topic
    m_decode=str(msg.payload.decode("utf-8","ignore"))
    #print("data Received type",type(m_decode))
    #print("data Received",m_decode)
    # print("Converting from Json to Object")
    m_in = json.loads(m_decode) #decode json data
    #print(type(m_in))
    voltage = m_in["StatusSNS"]["ENERGY"]["Voltage"]
    print(voltage)






client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, 1883, 60)
client.loop_start()


#put in overall while loop 
# ping the sonoff device for readings
# write the readings tot the gsheet

while True:
    print ("loop running")
    client.publish("cmnd/mospow2/STATUS", 10)
    # this little bugger below stuffed up my json validation!!!
    #client.publish("werkdit", "yep")
    time.sleep(5)

#kind of important to do the loop forever and must be last line


