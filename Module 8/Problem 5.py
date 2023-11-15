#Namirah
#11/15

#Write a function that checks whether your game character has picked up all the items needed to perform certain tasks and checks against any status debuffs. Confirm checks with print statements.

class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses
    def get_model(self):
        return self.nickname
    def get_year(self):
        return self.weapons
    def get_color(self):
        return self. weaknesses
    def profile(self):
        return self.nickname, self.weapons, self. weaknesses
player1 = character('','','')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']
for item in player1.weapons:
    print("Item: ", item)
for debuff in player1.weaknesses:
    print("Debuff: ", debuff)

def tasks(weapons, weaknesses):
    print("Task 1")
    if 'rope' in weapons and 'coat' in weapons and 'first aid kit' in weapons and 'slow' not in weaknesses:
        print("You can climb a mountain!")
    else:
        print("You can't climb a mountain")
    print("Task 2")
    if 'pan' in weapons and 'groceries' in weapons and 'small' not in weaknesses:
        print("Cook a meal")
    else:
        print("You can't cook a meal")
    print("Task 3")
    if 'pen' in weapons and 'paper' in weapons and 'idea' in weapons and 'confusion' not in weaknesses:
        print("You can write a book")
    else:
        print("You can't write a book")

tasks(player1.weapons, player1.weaknesses)