def factorial(num): #create a function
  fact = 1 #initialize factorial as 1
  for i in range(1,num+1): #loop to the number
      fact *=  i #keep multiplying untill the number is reached
  print (f"The factorial of {num} is: {fact}") #print the result

num = int(input("Enter a number: ")) #alternatively you could pass in an integer
factorial(num) #call the function
