import re #import regex
pattern = "(\w*oor|\w*ore)" #pattern to serach for
rhymingWords = [] #the rhyming words

with open("TheRaven.txt", "r") as f: #open the file
  for line in f: #read the lines
    rhymingWords.extend(re.findall(pattern, line, re.IGNORECASE)) #add the rhyming words

print(rhymingWords) #print the rhyming words
print(len(rhymingWords)) #print the amount of rhyming words
