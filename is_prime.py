"""checks if a number is prime"""
def isPrime(num):
    return 2 in [num, 2 ** num % num]

num= int (input())    
print(isPrime(num))
