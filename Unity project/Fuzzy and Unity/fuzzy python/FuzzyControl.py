
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import ReadJson as rj



####Set up the Fuzzy

#Set the Input
light = ctrl.Antecedent(np.arange(0, 780, 1), 'light')
soil = ctrl.Antecedent(np.arange(0, 100, 1), 'soil')
people = ctrl.Antecedent(np.arange(0,3,1),'people')
#Set the Output
valence = ctrl.Consequent(np.arange(0, 300, 1), 'valence')
arousal = ctrl.Consequent(np.arange(0, 300, 1), 'arousal')
# Auto-membership function population is possible with .automf(3, 5, or 7)
light.automf(3)
soil.automf(3)
people.automf(3)
#valence output
valence['low'] = fuzz.trimf(valence.universe, [0, 0, 150])
valence['medium'] = fuzz.trimf(valence.universe, [0, 150, 299])
valence['high'] = fuzz.trimf(valence.universe, [150, 299, 299])
#arousal output
arousal['low'] = fuzz.trimf(valence.universe, [0, 0, 150])
arousal['medium'] = fuzz.trimf(valence.universe, [0, 150, 299])
arousal['high'] = fuzz.trimf(valence.universe, [150, 299, 299])

#valence rules
rule1 = ctrl.Rule(light['poor'] | soil['poor'], valence['low'])
rule2 = ctrl.Rule(light['good'] | soil['poor'], valence['high'])
rule3 = ctrl.Rule(light['good'] | people['poor'], arousal['high'])

#valence Control
emotion_ctrl = ctrl.ControlSystem([rule1,rule2,rule3])
emotioning = ctrl.ControlSystemSimulation(emotion_ctrl)
  
  


# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
def Fuzzy():
    #ReadJson

    
     brightness, soilmoisture,count=rj.Read()
   #Fuzzy Caculating
     emotioning.input['light'] = brightness
     soilmoisture = mappct(soilmoisture, 1023,465, 0, 100)
     emotioning.input['soil'] = soilmoisture
  
     
     
     emotioning.input['people'] = count
     emotioning.compute()
     
     #Emotion Result
     valence = emotioning.output['valence'].item()
     arousal = emotioning.output['arousal'].item()
     emotion = None
     #emotion Control
     
     if valence > 200.0 and arousal <100.0:
         emotion = 'relaxation'
     elif valence > 200.0 and arousal >200.0:
         emotion = 'happy'
     elif valence < 100.0 and arousal >200.0:
         emotion = 'angry'
     elif valence < 100.0 and arousal <100.0:
         emotion = 'sad'
     else:
         emotion = 'normal'
    
         
     # Fuzzing output
     return emotion,brightness,soilmoisture,count
#soil moisture calculate reference  
#http://educ8s.tv/arduino-soil-moisture-sensor/
#https://www.jetmore.org/john/blog/2011/09/arduinos-map-function-and-numeric-distribution/     
def mappct(x, in_min, in_max, out_min, out_max):

  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;

   
   






