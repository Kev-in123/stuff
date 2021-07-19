"""checks if a number is prime"""
def isPrime(num):
    return 2 in [num, 2 ** num % num]

num = int(input()) #alternatively you could pass in a number    
print(isPrime(num))
