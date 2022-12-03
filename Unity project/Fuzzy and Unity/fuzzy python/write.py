import csv


def write(emotion,brightness,soilmoisture,count):
  row = [emotion,brightness,soilmoisture,count]
  csvFile = open('csv/data.csv', 'a')
  writer = csv.writer(csvFile)
  writer.writerow(row)
  csvFile.close()