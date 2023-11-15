#Namirah
#11/15

#Write a function that takes two inputs from a user and prints whether the sum is greater than 10, less than 10, or equal to 10

def compare():
    x = int(input("Enter a number"))
    y = int(input("Enter another number"))

    if x+y > 10:
        print("Sum is greater than 10")
    elif x+y < 10:
        print("Sum is less than 10")
    else:
        print("The sum is equal to 10")

compare()