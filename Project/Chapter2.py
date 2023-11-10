import MainGame
def start():
    MainGame.name = "Namirah"
    print("Name is now", MainGame.name)

    print("chapter 2 intro")

    print("wow, your painting is amazing!, said sarah")
    if MainGame.relationship >= 3:
        print("Sarah really likes you")
    choice = int(input("1. interact with fellow artist, 2.complete project alone, 3. ask Sarah for help"))

    if choice == 1:
        print("Artists invite you to art festival")
        choice2 = int(input("1.go with Sarah, 2. go with somebody else"))
        if choice2 == 1:
            MainGame.relationship += 1
        elif choice2 == 2:
            print("goes with another friend to the art festival")

    elif choice == 2:
        print("completes art project alone at home")

    elif choice == 3:
        print("Asks Sarah to help with art project")
        MainGame.relationship += 3

    print("finishes art project")

    import Chapter3
    Chapter3.start()