import re
text="H̙ͤ́e͍̤̠l̩͋͞l̸̈́̚o" #change this to the zalgo text
unzalgo=lambda word:re.sub("(?i)([aeiouy]̈)|[̀-ͯ҉]","\\1",word) #note that this method can't filter 𝔱𝔢𝔵𝔱 𝔩𝔦𝔨𝔢 𝔱𝔥𝔦𝔰 
print(unzalgo(text))

#line 3 can be replaced with:
unzalgo=lambda word:re.sub("[^a-zA-Z0-9 \n.]", "", text)
#but if 𝔱𝔢𝔵𝔱 𝔩𝔦𝔨𝔢 𝔱𝔥𝔦𝔰 is the string, there will be no output
