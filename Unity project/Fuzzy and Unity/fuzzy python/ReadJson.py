#Url getting
import requests 
#ambientroom
URL1 = "http://192.168.0.18/ambientroom"
#human Detection
URL2 = "http://192.168.0.4:5100/detection"


def Read():
    #reading ambient data
    ambientroom = requests.get(url = URL1) 
    AmData = ambientroom.json()
    brightness = float(AmData['light'][0])
    soilmoisture = float(AmData['soil_moisture'][0])
    #reading Human Detection
    
    detection = requests.get(url = URL2)
    DeData = detection.json()
    count = float(DeData['count'])
    
    #return data
    return brightness, soilmoisture, count



