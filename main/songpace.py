#Welcome, mangiatori di cazzi, to this thing I made out of pure boredom.
#Microwavedd :))

#This right here are the modules used, the first three are custom and can be found on the same folder as this file.
from typewriter import typeffect
from song import salyr  #Salir means "to get out" in spanish, making reference to you escape in portal, hehehehehehe
from broom import sweep  
import sys
import time

#What this does is disable the obnoxious message of "Hello from the Pygame co-" HALT DEIN MUND, DU KLEINER HAUFEN PFERDESCHEISSE
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame 
from pygame import mixer 
# it is important to import pygame after that
#By the way, pygame is the way of making the music work


#TODO hacer todo el pace de la cancion, siendo fiel el video original

#The music engine
mixer.init()
mixer.music.load('C:/Users/Ingo/Desktop/PortalStillAlive/main/StillAlive.mp3')

#The core of the project: The lyrics
typeffect("Forms FORM-29827281-12:\n",0.09)
typeffect("Test Assesment Report\n\n\n",0.09)
time.sleep(3)
mixer.music.play()
typeffect(salyr(0),0.09)
time.sleep(2)
typeffect(salyr(1),0.09)
time.sleep(0.3)
typeffect(salyr(2),0.14)
time.sleep(1)
typeffect(salyr(3),0.09)
typeffect(salyr(4),0.16)
time.sleep(2)
typeffect(salyr(5),0.12)
time.sleep(2)
typeffect(salyr(6),0.08)
typeffect(salyr(7),0.11)
time.sleep(1.6)
typeffect(salyr(8),0.11)
typeffect(salyr(9),0.08)
print("\n")
time.sleep(0.5)
time.sleep(5)

