import random
import time
import cayenne.client

def cayene(comptaPersonas):
    client.virtualWrite(1, comptaPersonas)

def lectura():
    comptaPersonas = random.randint(0, 1) 
    return comptaPersonas

comptaPersonas = 0

MQTT_USERNAME = "41d7a790-7c79-11e9-beb3-736c9e4bf7d0"
MQTT_PASSWORD = "0ea448345393a77dd056f6212f71801aae98749e"
MQTT_CLIENT_ID = "26497c80-8050-11e9-beb3-736c9e4bf7d0"
client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME,MQTT_PASSWORD, MQTT_CLIENT_ID)

while True:  
    client.loop()
    contador=0
    for x in range(60):
        contador += lectura() 
        print(contador) .                                 
        time.sleep(1) 
    cayene(contador)











































