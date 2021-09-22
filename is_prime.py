"""checks if a number is prime"""
def isPrime(num):
    return 2 in (num, 2 ** num % num) # at least one of the numbers will be 2

num = int(input()) #alternatively you could pass in a number    
print(isPrime(num)) #print

