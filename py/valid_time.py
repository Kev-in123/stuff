"""check if a time is valid with the `hh:mm:ss xx` format"""
import re

# checks if the hh:mm:ss: xx is valid
time_regex = re.compile(r"(0[1-9]|1[0-2]):[0-5][0-9]:[0-5][0-9] ([AP]M)") 
def valid_time(time: str):
    # return if the string passes the regex or not
    return bool(time_regex.match(time)) 

# alternatively you could pass in a string
time = input() 
print(valid_time(time)) 
