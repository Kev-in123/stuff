import re
import unicodedata
text = input(">")  #alternatively you could pass in a string
text = unicodedata.normalize("NFKC", text)
unzalgo = lambda text: re.sub("[^a-zA-Z0-9 \n.]", "", text)
print(unzalgo(text))
