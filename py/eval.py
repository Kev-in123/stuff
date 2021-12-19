"""safely use eval() in python great as a caculator app"""

env = {          # disable stuff for safety
  "locals": None,
  "globals": None,
  "__name__": None,
  "__file__": None,
  "__builtins__": None
  }
code = input() # alternatively you could pass in a string
eval(code, env)  

