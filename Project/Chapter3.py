import MainGame
def start():
    print(MainGame.name)

    print("chapter 3 into")

    print("Can I balance my art and love? Am I deserving of these relationships?")
    chosen = False
    while chosen == False:
        choice = int(input("1. date Sarah, 2.Sarah asks me out for dinner, 3. continue focusing on art"))

        if choice == 3:
            print("You focus on your art")
            chosen = True
            import Chapter5
            Chapter5.start()
        else:
            if choice == 1:
                print("You ask Sarah on a date")
                MainGame.relationship += 3
                chosen = True

            elif choice == 2:
                print("Sarah asks you out on a date")
                MainGame.relationship += 1
                chosen = True
        print("set a time for dinner date")

        import Chapter4
        Chapter4.start()