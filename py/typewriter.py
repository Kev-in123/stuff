message = input() # alternatively you could pass in a string
def typewriter(msg):  
    for char in msg:  # loop through the string
        print(char, end="", flush=True) # print the characters and flush them for a typewriter effect
        
typewriter(message) 
