#Namirah
#11/15

#Write a function that takes a year as a parameter and returns True if the year is leap year, False if it is otherwise

def leap (year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False