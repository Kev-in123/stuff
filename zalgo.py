import random

message = input(">")

def zalgo(string):
  for char in string:
    if char ==" ":
      string+=" "
    else:
      intensity=3
      for i in range(intensity):
        zalgo_char=random.choice(range(768, 879))
        string+=chr(zalgo_char)
      string+=char
  half=int(len(string)/4)
  word=string[half:]
  return word

print(zalgo(string))

