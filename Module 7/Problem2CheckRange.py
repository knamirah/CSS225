#Namirah
#11/8/2023

#Write a Python function to check whether a number is in a given range. Use range(1,10). Print whether the number is in or not in the range.
def checkinrange(number):
    for n in range(1, 10):
        if number == n:
            return print("number is in range")
    else:
        return print("number not in range")

checkinrange(7)
