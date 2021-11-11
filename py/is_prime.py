"""checks if a number is prime"""
def isPrime(num):
    if (num < 2):
      return False
    elif (num == 2):
      return True
    return 2 ** num % num == 2 # at least one of the numbers will be 2

num = int(input()) #alternatively you could pass in a number    
print(isPrime(num)) #print
