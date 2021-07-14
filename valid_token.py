"""validates a discord token"""
import re

token_regex = re.compile(r"[a-zA-Z0-9_-]{23,28}\.[a-zA-Z0-9_-]{6,7}\.[a-zA-Z0-9_-]{27}")

def valid_token(token: str):
        return bool(token_regex.match(token))
  
token = input(">") #alternatively you could pass in a string
print(valid_token(token)) 
