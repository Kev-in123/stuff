message = input(">") #alternatively you could pass in a string
def typewriter(msg):  
  for char in msg:  
    print(char,end="",flush=True)
typewriter(message) 
