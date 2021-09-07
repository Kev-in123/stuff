"""check if a time is valid with the `hh:mm:ss xx` format"""
import re #regex for validation

time_regex = re.compile(r"(0[1-9]|1[0-2]):[0-5][0-9]:[0-5][0-9] ([AP]M)") #checks if the hh:mm:ss: xx is valid

def valid_time(time: str):
    return bool(time_regex.match(time)) #return if the emoji passes the regex or not

time = input() #alternatively you could pass in a string
print(valid_time(time)) 
