import re

time_regex=re.compile(r"(0[1-9]|1[0-2]):[0-5][0-9]:[0-5][0-9] ([AP]M)")

def valid_time(time: str):
    return bool(time_regex.findall(time))

print(valid_time("10:10:10 PM"))