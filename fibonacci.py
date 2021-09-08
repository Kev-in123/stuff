"""fibonacci in python"""

def calculate(n: int): #function defenition

    if n == 2 or n == 1: #check if the number requested is the forst or second number
        return 1
    
    r1 = 1 #initialize stuff
    r2 = 1
    r = 0
    for i in range(n-2): #loop the the number
          r = r1 + r2 #calculate stuff
          r2 = r1
          r1 = r
    return r #return the number

num = int(input("Enter the number: ")) #prompt for a number; alternatively you could pass in an integer
print(calculate(num)) #call the function
