#WAP to find the sum of first  n numbers. (using while)
n = int(input("Enter your n"))

sum = 0
i = 1
while i <= n:
      sum += i
      i += 1
print("The sum is", sum) 
 
# using for loop                   n = 7
#                                  sum = 0
#                                  for i in range  (1, n+1)
#                                       sum += i
#                                  print("Total sum = ", sum) '''



#WAP to find the factorial of first n numbers.(using for)
n = int(input("Enter your n"))
fact = 1
i = 1
while i <= n:
    fact*= i
    i += 1
print("The factorial is", fact) 


