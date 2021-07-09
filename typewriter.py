"""enter some text and have it printed in a typewriter style"""
message = input(">") #alternatively you could pass in a string
def typewriter(msg):  
  for char in msg:  
    print(char,end="",flush=True)
typewriter(message) 
