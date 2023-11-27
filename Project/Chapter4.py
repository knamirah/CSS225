import MainGame
def start():
    print()

    print("chapter 4 into")

    print("How has your day been?")
    chosen = False
    while chosen == False:
        choice = int(input("1. discuss long term goals as a couple, 2. plans future wedding with Sarah, 3. still thinking about my career"))
        if choice == 1:
            print("discuss long term goals as a couple")
            MainGame.relationship += 1
            chosen = True

        elif choice == 2:
            print("plans future wedding with Sarah")
            MainGame.relationship += 3
            chosen = True
        elif choice == 3:
            print("still thinking about my career")


    import Chapter5
    Chapter5.start()
