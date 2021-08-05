import mxnet as mx
import numpy as np
from mxnet.gluon.data.vision import transforms

import json

import paho.mqtt.client as paho

published=False

def on_connect(mqtt_client, obj, flags, rc):
    if rc==0:
        print("connected")
    else:
        print("connection refused")

def on_publish(client, userdata, mid):
    print("published data")
    global published
    published=True

def get_image(path, show=False):
    img = mx.image.imread(path)
    if img is None:
        return None
    return img

def preprocess(img):
    transform_fn = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    img = transform_fn(img)
    img = img.expand_dims(axis=0)
    return img



broker = "127.0.0.1"
client = paho.Client("cl_preprocessor")
client.on_connect=on_connect
client.on_publish=on_publish
client.connect(broker)
choice = 1
client.loop_start()

if choice == 1:
    img_path = 'kitten.jpg'
    img = get_image(img_path, show=True)
    img = preprocess(img)
    print(img.shape)
    img = mx.ndarray.array(img).asnumpy().tolist()
    data = {'choice': choice,'data': img}
    payload = json.dumps(data)
    client.publish("cl_preprocess_out", payload, qos=0)

while not published:
    pass