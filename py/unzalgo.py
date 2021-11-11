"""remove zalgo from text including words like 𝓽𝓱𝓮𝓼𝓮"""

import re #importd
import unicodedata

text = input()  #alternatively you could pass in a string
text = unicodedata.normalize("NFKC", text) #normalize the string
def unzalgo (text): #create a function
  return re.sub("[^a-zA-Z0-9 \n.]", "", text) #reges to fix things

print(unzalgo(text))
