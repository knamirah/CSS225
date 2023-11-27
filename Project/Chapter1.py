import MainGame
def start():
    print("Name starts as ", MainGame.name)

    print("chapter one intro")

    print("“Hi there! I'm Sarah. Nice to meet you!""")
    chosen = False
    while chosen == False:
        choice = int(input("1. invite sarah inside, 2. hold a house warming party, 3. practice art class alone"))

        if choice == 1:
            print("come inside, have lunch")
            MainGame.relationship += 3
            chosen = True
        elif choice == 2:
            print("invited the neighborhood friends over")
            MainGame.relationship += 1
            chosen = True
        elif choice == 3:
            print("worked on my art painting")
            chosen = True

    print("Sarah invites you to an art class")
    print("Your relationship with Sarah is now", MainGame.relationship)

    import Chapter2
    Chapter2.start()