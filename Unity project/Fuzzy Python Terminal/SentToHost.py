from flask import Flask
import FuzzyControl as fc
import write as w

app = Flask(__name__)

emotionN = None


@app.route("/")
def home():
    #Get data from Fuzzy control system
    emotion,brightness,soilmoisture,count,valence,arousal,valenceN,arousalN = fc.Fuzzy()
    
    #define Emotion Number
    if emotion == "happy":
        emotionN = 5
    elif emotion == "relaxation":
        emotionN = 4
    elif emotion == "normal":
        emotionN = 3
    elif emotion == "angry":
        emotionN = 2
    elif emotion == "sad":
        emotionN = 1
    
    
    # 1 = LOw , 2 == Medium , 3==HIGH
    
    
    
    
       
    #write to csv
    w.write(emotion,emotionN,brightness,soilmoisture,count,valence,arousal,valenceN,arousalN)
    #return Json
    return {"emotion":emotion,"emotionN":emotionN,"brightness":brightness,"soilmoisture":soilmoisture,"count":count,"valence":valence,"arousal":arousal,"valenceN":valenceN,"arousalN":arousalN}
    
if __name__ == "__main__":
    app.run(debug=True,host = '0.0.0.0')
    
    
