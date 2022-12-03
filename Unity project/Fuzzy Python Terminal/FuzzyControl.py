
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import ReadJson as rj


valenceN = None
arousalN = None
####Set up the Fuzzy

#Set the Input
light = ctrl.Antecedent(np.arange(0, 100, 1), 'light')
soil = ctrl.Antecedent(np.arange(0, 100, 1), 'soil')
people = ctrl.Antecedent(np.arange(0,100,1),'people')
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

#Arousal rules
#High
rule1 = ctrl.Rule(light['poor'] & soil['poor'] | 
                  light['good'] & soil['average'] |
                  light['good'] & soil['good']  |
                  
                  light['poor'] & people['poor'] |
                  light['good'] & people['good'] |
                  light['average'] & people['good'] |
                  
                  soil['poor'] & people['poor'] |
                  soil['good'] & people['poor'] |
                  soil['good'] & people['good']
                  
                  , arousal['high'])

#Medium
rule2 = ctrl.Rule(light['average'] & soil['good'] | 
                  light['average'] & soil['poor'] |
                  light['good'] & soil['poor']  |
                  light['poor'] & soil['good']  |
                  
                  light['good'] & people['average'] |
                  light['average'] & people['average'] |
                  light['poor'] & people['good'] |
                  light['good'] & people['poor'] |
                  
                  soil['poor'] & people['average'] |
                  soil['average'] & people['good'] 
                 
                  
                  , arousal['medium'])

#low
rule3 = ctrl.Rule(light['poor'] & soil['average'] | 
                  light['average'] & soil['average'] |
                  
                  
                  light['poor'] & people['average'] |
                  light['average'] & people['poor'] |
                  
                  
                  soil['average'] & people['poor'] |
                  soil['good'] & people['average'] 
                  
                  
                  , arousal['low'])
                  
                  
#valence rules
#High
rule4 = ctrl.Rule(light['average'] & soil['average'] | 
                  light['good'] & soil['average'] |
                  
                  
                  light['good'] & people['good'] |
                  light['good'] & people['average'] |
                  
                  
                  soil['average'] & people['average'] |
                  soil['average'] & people['good'] 
                  
                  
                  , valence['high'])

rule5 = ctrl.Rule(light['poor'] & soil['average'] | 
                  light['good'] & soil['poor'] |
                  light['good'] & soil['good'] |
                  
                  
                  light['good'] & people['poor'] |
                  light['average'] & people['average'] |
                  light['poor'] & people['average'] |
                  light['poor'] & people['good'] |
                  
                  
                  soil['good'] & people['good'] |
                  soil['good'] & people['average'] |
                  soil['average'] & people['poor'] |
                  soil['poor'] & people['good'] 
                  
                  
                  , valence['medium'])


rule6 = ctrl.Rule(light['poor'] & soil['poor'] | 
                  light['average'] & soil['poor'] |
                  light['poor'] & soil['good'] |
                  light['average'] & soil['good'] |
                  
                  
                  light['poor'] & people['poor'] |
                  light['average'] & people['poor'] |
                  
                  
                  
                  soil['good'] & people['poor'] |
                  soil['poor'] & people['average'] |
                  
                  soil['poor'] & people['poor'] 
                  
                  
                  , valence['low'])

#rule1 = ctrl.Rule(light['poor'] | soil['poor'], valence['low'])
#rule2 = ctrl.Rule(light['good'] | soil['poor'], valence['high'])
#rule3 = ctrl.Rule(light['good'] | people['poor'], arousal['high'])


#valence Control
emotion_ctrl = ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6])
emotioning = ctrl.ControlSystemSimulation(emotion_ctrl)
  
  


# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
def Fuzzy():
    #ReadJson

    
     brightness, soilmoisture,count=rj.Read()
   #Fuzzy Caculating
     brightness = mappct(brightness, 0,680, 0, 100) ##Mapping to Percentage
     emotioning.input['light'] = brightness
     
     #wet 1800, dry 3200
     soilmoisture = mappct(soilmoisture, 3100,1800, 0, 100)##Mapping to Percentage
     #soilmoisture = mappct(soilmoisture, 2600,1800, 0, 100)
     emotioning.input['soil'] = soilmoisture
  
     
     count = mappct(count, 0,4, 0, 100)##Mapping to Percentage
     emotioning.input['people'] = count
     
     
     emotioning.compute()
     
     #Emotion Result
     valence = emotioning.output['valence'].item()
     arousal = emotioning.output['arousal'].item()
     emotion = None
     #emotion Control
     """
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
     """
     if valence <150:
        valenceN  = 1 #Low
     elif  valence ==150 :
        valenceN =2 #Medium
     elif valence > 150:
        valenceN = 3  #High
    
     if arousal <150:
        arousalN  = 1#Low
     elif valence == 150:
        arousalN =2   #Medium
     elif arousal > 150:
        arousalN = 3   #High
    
    
    
    
    
    
    
    
    
    
    
    
     if valenceN ==3 and arousalN ==1:
         emotion = 'relaxation'
     elif valenceN == 3 and arousalN == 3:
         emotion = 'happy'
     elif valenceN  == 1 and arousalN  == 3:
         emotion = 'angry'
     elif valenceN == 1 and arousalN  == 1:
         emotion = 'sad'
     else:
         emotion = 'normal'

         
    
         
         
         
     # Fuzzing output
     return emotion,brightness,soilmoisture,count,valence,arousal,valenceN,arousalN
#soil moisture calculate reference  
#http://educ8s.tv/arduino-soil-moisture-sensor/
#https://www.jetmore.org/john/blog/2011/09/arduinos-map-function-and-numeric-distribution/     
def mappct(x, in_min, in_max, out_min, out_max):

  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;

   
   






