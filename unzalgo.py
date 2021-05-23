import re
text="H̙ͤ́e͍̤̠l̩͋͞l̸̈́̚o" #change this to the zalgo text
text = unicodedata.normalize("NFKC", text)
unzalgo=lambda word:re.sub("[^a-zA-Z0-9 \n.]", "", text)
print(unzalgo(text))
