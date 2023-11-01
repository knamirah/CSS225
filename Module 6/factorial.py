#Namirah
#10/30

#Use a for statement to calculate the factorial of a user input value. Print this value as well as the calculated value using the factorial function in the math module
#factorial example: 5! = 5 * 4 * 3 * 2 * 1

import math

n = int(input("Enter a number"))
print(n)

print("factorial:", math.factorial(n))
answer = 1
for i in range(n):
    answer *=i +1


print("for loop:", answer)