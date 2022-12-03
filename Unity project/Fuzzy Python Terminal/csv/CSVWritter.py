import csv
import time
import requests 
#ambientroom
URL = "http://192.168.0.4:5000/"



def write():
    data = requests.get(url = URL) 
    CSVData = data.json()
    brightness = float(CSVData['brightness'])
    soilmoisture = float(CSVData['soilmoisture'])
    count = float(CSVData['count'])
    emotion = CSVData['emotion']
    
    
    strHMS = time.strftime("%H:%M:%S") #time.ctime()
    row = [strHMS,emotion,count,brightness,soilmoisture]
    csvFile = open('csv/data.csv', 'a', newline='\n')
    writer = csv.writer(csvFile)
    writer.writerow(row)
    csvFile.close()

while 1:
    write()  
 
    
    
    
 
