import time

groccery_list = [];

def DelSequence():
    print("Please tell which element you would like to delete!")

    for i in range( len(groccery_list) ):
        print("[", ( i + 1), "]",  groccery_list[i])

    option = int(input("Select the element you'd like to delete: "))

    while True:
        if groccery_list[option - 1]:
            groccery_list.pop(option - 1)
            print("Successfully deleted that option! Going back to menu...")
            time.sleep(1)
            break
        else:
            print("Are you sure this exists?")
    ShowStart()

def AddSequence():
    while True:
        try:
            groccery = input("Please provide the groccery: ")

            if groccery == "end":
                print("Got it! Let's see the list...")
                print(groccery_list)
                break

            groccery_list.append(groccery)
        except:
            print("An exception has occured!")
    ShowStart()

def ShowList():
    print("Here is the list! To go back to the menu, type [ END ]!")

    for i in range( len(groccery_list) ):
        print("[", ( i + 1), "]",  groccery_list[i])

    while True:
        option = input("Your choice: ")
        if option.lower() == "end":
            ShowStart()
            break
        else:
            print("unknown command?")

def ShowStart():
    print("\033[H\033[2J", end="")
    print("Welcome to the grocerry list program!")
    print("Please provide what you want to do:")
    print("[ ADD ] to add stuff to the list!")
    print("[ DELETE ] to delete stuff from the list!")
    print("[ SHOW ] to show the list")

    option = input("Your choice: ")

    match option.lower():
        case "add":
            AddSequence()

        case "show":
            ShowList()

        case "delete":
            DelSequence()

        case _:
            print("Unknown command?")
            time.sleep(1)
            ShowStart()

ShowStart()