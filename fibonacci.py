def calculate(n: int):

    if n ==2 or n ==1:
      return 1
    
    r1 = 1
    r2 = 1
    r = 0
    for i in range(n-2):
      r = r1 + r2
      r2 = r1
      r1 = r

print(calculate(15))