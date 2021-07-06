import re
import unicodedata
text=input(">")  #alternatively you could pass in a string
text = unicodedata.normalize("NFKC", text)
unzalgo=lambda word:re.sub("[^a-zA-Z0-9 \n.]", "", text)
print(unzalgo(text))
