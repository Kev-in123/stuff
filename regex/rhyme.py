import re

pattern = "(\w*oor|\w*ore)"
rhymingWords = []

with open("TheRaven.txt", "r") as fi:
  for line in fi:
    rhymingWords.extend(re.findall(pattern, line, re.IGNORECASE))

print(rhymingWords)
print(len(rhymingWords))
