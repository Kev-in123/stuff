"""validates a discord emoji (the server ones)"""
import re

# checks if the emoji is animated or not, then matches an emoji name, and finally the id
emoji_regex = re.compile(r"<a*:[a-zA-Z0-9]+:[0-9]{18}>") 

def valid_emoji(emoji: str):
    # return if the emoji passes the regex or not
    return bool(emoji_regex.match(emoji)) 
  
# alternatively you could pass in a string
emoji = input() 
print(valid_emoji(emoji)) 
