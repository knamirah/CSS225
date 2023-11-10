import MainGame
def start():
    print(MainGame.name)

    print("chapter 3 into")

    print("Can I balance my art and love? Am I deserving of these relationships?")

    choice = int(input("1. date Sarah, 2.Sarah asks me out for dinner, 3. continue focusing on art"))

    if choice == 3:
        print("You focus on your art")
        import Chapter5
        Chapter5.start()
    else:
        if choice == 1:
            print("You ask Sarah on a date")

        elif choice == 2:
            print("Sarah asks you out on a date")
        print("set a time for dinner date")
        import Chapter4
        Chapter4.start()