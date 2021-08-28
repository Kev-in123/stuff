"""remove zalgo from text including words like 𝓽𝓱𝓮𝓼𝓮"""

import re
import unicodedata
text = input()  #alternatively you could pass in a string
text = unicodedata.normalize("NFKC", text)
def unzalgo (text):
  return re.sub("[^a-zA-Z0-9 \n.]", "", text)

print(unzalgo(text))
