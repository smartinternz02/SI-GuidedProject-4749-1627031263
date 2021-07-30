import wiotp.sdk.device
import time
import random
import requests
myConfig = { 
    "identity": {
        "orgId": "1smyiq",
        "typeId": "Asish",
        "deviceId":"8788"
    },
    "auth": {
        "token": "Ashish@123"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    temp=random.randint(-20,125)
    pul=random.randint(50,120)
    bp=random.randint(50,200)
    myData={'temperature':temp, 'pulse':pul, 'BP':bp}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    
    if(pul>100 or pul<60):
        print("successfully information sent")
        r=requests.get('https://www.fast2sms.com/dev/bulkV2?authorization=tzlaoNKv97qepdxPi0HnuDZME4FQgVS58UJWL6k3RAbsTXIwGORxoFqhXLnUkcPrbCZjwH5O4A2t8TYl&route=q&message=health%20condition%20is%20critical&language=english&flash=0&numbers=7337314831')
        print(r.status_code)
        
    
        
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
