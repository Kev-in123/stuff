string='message' #change this to the string you want
def typewriter(msg):  
  for char in msg:  
    print(char,end="",flush=True)
typewriter(string) 