import time
import json
import numpy as np
import paho.mqtt.client as paho



def on_message(clientname, userdata, message):
    time.sleep(1)
    data = json.loads(message.payload.decode('utf-8'))
    global choice
    choice = data['choice']
    global score, disp
    if choice == 1:
        scores = np.array(data['scores']).astype('float32')
        
        disp=True


def on_connect(mqtt_client, obj, flags, rc):
    if rc==0:
        client.subscribe("cl_inference_out", qos=0)
        print("connected")
    else:
        print("connection refused")


broker = "127.0.0.1"
client = paho.Client("cl_postprocessor")
client.on_message=on_message
client.on_connect=on_connect
client.connect(broker)
client.loop_start()
while 1:
    pass
