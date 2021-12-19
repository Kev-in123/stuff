"""validates a discord token"""
import re 

# cheks character length, ids, and timestamps
token_regex = re.compile(r"[a-zA-Z0-9_-]{23,28}\.[a-zA-Z0-9_-]{6,7}\.[a-zA-Z0-9_-]{27}") 

def valid_token(token: str):
    # return if the string passes the regex or not
    return bool(token_regex.match(token)) 
  
# alternatively you could pass in a string
token = input() 
print(valid_token(token)) 
