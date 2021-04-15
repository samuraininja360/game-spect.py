import math
import time

def distance(sprite1, sprite2):
  return math.sqrt((sprite1[0]-sprite2[0])*(sprite1[0]-sprite2[0])+(sprite1[1]-sprite2[1])*(sprite1[1]-sprite2[1]))

mySprite = [0,0,100,100]
