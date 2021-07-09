"""check if a time is valid with the `hh:mm:ss xx` format"""
import re

time_regex=re.compile(r"(0[1-9]|1[0-2]):[0-5][0-9]:[0-5][0-9] ([AP]M)")

def valid_time(time: str):
    return bool(time_regex.match(time))

time=input(">") #alternatively you could pass in a string
print(valid_time(time)) 
