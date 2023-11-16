#Namirah
#11/16

#Using a while loop, ask the user to enter a number. Append each entered number to a list and add them together. Continue asking for a number until the sum of the list of numbers is greater than 100.

list = []
sum = 0

while sum <= 100:
    x = int(input("Enter a number"))
    list.append(x)
    sum += x

print("Sum of number", sum)
print("List of numbers", list)
