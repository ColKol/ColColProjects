#TI Innovator Hub Cooling System
# Hub Project
#================================
from ti_hub import *
from math import *
from time import sleep
from ti_plotlib import text_at,cls
from ti_system import * #asterisk imports everything
#================================

clear_history()

#Define Inputs & Outputs
TempSensor = dht("IN 1")
IRSensor = digital("IN 2")
Fan =squarewave("OUT 1")

#Light = bb_port(1)
#Peltier = bb_port(2)

#Peltier.write_port(1,2)
#Light.write_port(1,2)
#Light.write_port(1,2)

Light = digital("BB 1")

Peltier = digital("BB 3")

#Variables
HIThreshold = 32
CheckFrequency = 5

#Calculate heat index
def GetHeatIndex(t, RH):
  T = (t * 1.8) + 32 #convert celcius to farenheit
  
  HIF = -42.379 + 2.04901523*T + 10.14333127*RH - .22475541*T*RH - .00683783*T*T - .05481717*RH*RH + .00122874*T*T*RH + .00085282*T*RH*RH - .00000199*T*T*RH*RH
  HI = (HIF - 32) * (5 / 9)
  return HI

#Big loop
Loop = True
while(Loop):
  
  #Checking temperature
  while get_key() != "esc":
    clear_history()
    
    (t, h) = TempSensor.t_h_measurements()
    i = IRSensor.measurement()
    HI = GetHeatIndex(t, h)
    
    print(" ")
    print("Temp: " + str(t))
    print("Humidity: " + str(h))
    print("Heat Index: " + str(HI))
    print("IR: " + str(i))
    
    if HI >= HIThreshold: #and i == 1
      print("Status: Dangerous level of heat")
      Peltier.on()
      Fan.set(300,30,CheckFrequency)
      
      #alarm
      for i in range (0, CheckFrequency, 2):
        sound.tone(440, 1)
        Light.on()
        sleep(1)
        Light.off()
        sleep(1)
      
    else:
      print("Status: Safe level of heat")
      Light.off() #make this 0
      Peltier.off()
      sleep(CheckFrequency)
  
  #Exit
  print(" ")
  Exit = input("Exit program?: ")
  Exit = Exit.lower()
  if Exit == "yes":
    break
  
  #Change Heat
  print(" ")
  ChangeHeat = input("Change temperature threshold? ")
  ChangeHeat = ChangeHeat.lower()

  if ChangeHeat == "yes":
    NewThreshold = input("New temperature (default: 32C˚, current: " + str(HIThreshold) + "C˚): ")
    NewThreshold = int(NewThreshold)
    HIThreshold = NewThreshold
  
  #Change Frequency
  print(" ")
  ChangeFrequency = input("Change frequency of temperature check? ")
  ChangeFrequency = ChangeFrequency.lower()
  
  if ChangeFrequency == "yes":
    NewFrequency = input("New frequency (default: 2s, current: " + str(CheckFrequency) + "s): ")
    NewFrequency = int(NewFrequency)
    CheckFrequency = NewFrequency
