"""validates a discord emoji"""
import re #regex for validation

emoji_regex = re.compile(r"<a*:[a-zA-Z0-9]+:[0-9]{18}>") #checks if the emoji is animated or not, then matches an emoji name, and finally the id

def valid_emoji(emoji: str):
    return bool(emoji_regex.match(emoji)) #return if the emoji passes the regex or not
  
emoji = input() #alternatively you could pass in a string
print(valid_emoji(emoji)) 
