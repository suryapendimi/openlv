# mqqt example, Robert Brown, London South Bank University, 27.06.2018

import paho.mqtt.client as mqtt
import time, datetime, random


time_now = datetime.datetime.now()
def timestampPrint(msg):
    time_now = datetime.datetime.now()
    print(f"{time_now}: {msg}")

def msg_callback(client, userdata, message):
    msg = message.payload.decode("utf-8")
    timestampPrint(f"new message received on topic {message.topic}: \"{str(msg)}\"")


#set up mqtt client instance
client = mqtt.Client("orxa")
client.on_message=msg_callback 

#connect to server
broker_address="broker.hivemq.com" #for TESTING only - see www.mqtt-dashboard.com
client.connect(broker_address)
timestampPrint(f"connected to mqtt server at {broker_address}")
client.loop_start() #start the loop

#subscribe to topic
topic = "orxa/openlv/test1"
client.subscribe(topic)
timestampPrint(f"subcribed to topic {topic}")

feeder_no = random.randint(1,10)
feeder_location = random.choice(["factory", "substation", "feeder pillar"])
message = f"voltage violation on feeder {feeder_no} at {feeder_location} {random.randint(1,10)}"
client.publish("orxa/openlv/test1",message)
timestampPrint(f"published message on topic {topic}")

timestampPrint(f"listening for messages for the next 5 seconds")
time.sleep(4) # wait
client.loop_stop() #stop the loop
timestampPrint(f"stopped listening for messages")