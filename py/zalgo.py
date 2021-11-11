"""enter some text and have it printed with zalgo"""

import random

message = input() #alternatively you could pass in a string

def zalgo(string): 
  for char in string: #loop through the word
    if char == " ": #skip spaces
      string += " "
    else:
      intensity = 3
      for _ in range(intensity):
        zalgo_char = random.choice(range(768, 879)) #magik
        string += chr(zalgo_char)
      string += char
  half = int(len(string)/4)
  return string[half:]

print(zalgo(string))
