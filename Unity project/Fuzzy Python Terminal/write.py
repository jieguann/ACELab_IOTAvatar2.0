import csv
import time



def write(emotion,emotionN,brightness,soilmoisture,count,valence,arousal,valenceN,arousalN):
  strHMS = time.strftime("%H:%M:%S") #time.ctime()
  
  row = [strHMS,emotion,emotionN,count,brightness,soilmoisture,valenceN,arousalN,valence,arousal]
  csvFile = open('csv/data.csv', 'a', newline='\n')
  writer = csv.writer(csvFile)
  writer.writerow(row)
  csvFile.close()
