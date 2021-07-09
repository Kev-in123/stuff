"""remove zalgo from text als words like 𝓽𝓱𝓮𝓼𝓮"""

import re
import unicodedata
text = input(">")  #alternatively you could pass in a string
text = unicodedata.normalize("NFKC", text)
unzalgo = lambda text: re.sub("[^a-zA-Z0-9 \n.]", "", text)
print(unzalgo(text))
