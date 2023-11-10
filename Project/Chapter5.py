import MainGame
print("Uh oh!")
def start():
    print()

    print("chapter 5 into")

    print("I care about you deeply.")
    if MainGame.relationship == 12:
        print("You marry Sarah")
    elif 5 < MainGame.relationship < 11:
        print("You and Sarah go steady")
    elif 0 < MainGame.relationship <= 5:
        print("You and Sarah break up")
    else:
        print("There wasn't anything between you and Sarah")

def end():
    print("Blank")
    #end()