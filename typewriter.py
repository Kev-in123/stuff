message = input(">")
def typewriter(msg):  
  for char in msg:  
    print(char,end="",flush=True)
typewriter(message) 
