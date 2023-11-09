#Namirah
#11/8/2023

#Write a Python function that takes a list of numbers and returns a new list with unique elements of the first list. Use list [1, 3, 3, 3, 6, 2, 3, 5]. Use the append function.

def uniqueelements(input_list):
    unique_list = []
    for n in input_list:
        if n not in unique_list:
            unique_list.append(n)
    print(unique_list)

uniqueelements([1, 3, 3, 3, 6, 2, 3, 5])