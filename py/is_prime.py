"""checks if a number is prime"""
def isPrime(num):
    if (num < 2):
      return False
    elif (num == 2):
      return True
    return 2 ** num % num == 2 # this will return true for most cases

num = int(input()) # alternatively you could pass in a number    
print(isPrime(num))
