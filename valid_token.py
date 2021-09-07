"""validates a discord token"""
import re #regex for validation

token_regex = re.compile(r"[a-zA-Z0-9_-]{23,28}\.[a-zA-Z0-9_-]{6,7}\.[a-zA-Z0-9_-]{27}") #cheks character length, ids, and timestamps

def valid_token(token: str):
    return bool(token_regex.match(token)) #return if the emoji passes the regex or not
  
token = input() #alternatively you could pass in a string
print(valid_token(token)) 
