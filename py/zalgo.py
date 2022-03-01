"""enter some text and have it printed with zalgo"""

import random

def zalgo(string): 
  # loop through the word
  for char in string:
    # skip spaces 
    if char == " ": 
      string += " "
    else:
      intensity = 3
      for _ in range(intensity):
        # magik
        zalgo_char = random.choice(range(768, 879))
        string += chr(zalgo_char)
      string += char
  half = len(string)//4
  return string[half:]

message = input() # alternatively you could pass in a string
print(zalgo(message))

