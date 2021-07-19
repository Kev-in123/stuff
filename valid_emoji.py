"""validates a discord emoji"""
import re

emoji_regex = re.compile(r"<a*:[a-zA-Z]+:[0-9]{18}>")

def valid_emoji(emoji: str):
    return bool(emoji_regex.match(emoji))
  
emoji = input() #alternatively you could pass in a string
print(valid_emoji(emoji)) 
