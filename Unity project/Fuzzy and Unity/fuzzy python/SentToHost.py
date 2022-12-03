from flask import Flask
import FuzzyControl as fc
import write as w

app = Flask(__name__)

@app.route("/")
def home():
    #Get data from Fuzzy control system
    emotion,brightness,soilmoisture,count = fc.Fuzzy()
    #write to csv
    w.write(emotion,brightness,soilmoisture,count)
    #return Json
    return {"emotion":emotion,"brightness":brightness,"soilmoisture":soilmoisture,"count":count}
    
if __name__ == "__main__":
    app.run(debug=True,host = '0.0.0.0')