import sys, platform, os

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

__license__ = open("LICENSE","r").read()

pos = {
    "1":{"1": " ", "2": " ", "3": " ",},
    "2":{"1": " ", "2": " ", "3": " ",},
    "3":{"1": " ", "2": " ", "3": " ",}
    }

pos_clear = {
    "1":{"1": " ", "2": " ", "3": " ",},
    "2":{"1": " ", "2": " ", "3": " ",},
    "3":{"1": " ", "2": " ", "3": " ",}
    }

def menu():
    clear()
    print("="*30)
    print("= "+"Welcome to Tic Tac Toe!".center(26)+" =")
    print("="*30+"\n")
    print("select an option below")
    print("1 = Player vs Player")
    print("2 = License")
    print("3 = Exit")
    inp = input("> ")

    if inp == "1":
        clear()
        P1()
    elif inp == "2":
        clear()
        print(__license__)
        print("\nPress 'enter' to return to menu")
        input()
        menu()
    elif inp == "3":
        sys.exit()
    else:
        print("Invalid keyword, press 'enter' to return to menu\n")
        input()
        menu()

def test():
    comb = [pos["1"]["1"]+pos["1"]["2"]+pos["1"]["3"],
       pos["2"]["1"]+pos["2"]["2"]+pos["2"]["3"],
       pos["3"]["1"]+pos["3"]["2"]+pos["3"]["3"],
       pos["1"]["1"]+pos["2"]["1"]+pos["3"]["1"],
       pos["1"]["2"]+pos["2"]["2"]+pos["3"]["2"],
       pos["1"]["3"]+pos["2"]["3"]+pos["3"]["3"],
       pos["1"]["1"]+pos["2"]["2"]+pos["3"]["3"],
       pos["3"]["1"]+pos["2"]["2"]+pos["1"]["3"]]

    if "OOO" in comb:
        print("PLAYER 1 WON!")
        ask()
    elif "XXX" in comb:
        print("PLAYER 2 WON!")
        ask()

    for x in pos:
        if x != " ":
            places_taken +=1
    if places taken == 9:
        print("GAME OVER NO ONE WON")
        ask()
def display():
    print("\n[{0}][{1}][{2}]".format(pos["1"]["1"],pos["2"]["1"],pos["3"]["1"]))
    print("[{0}][{1}][{2}]".format(pos["1"]["2"],pos["2"]["2"],pos["3"]["2"]))
    print("[{0}][{1}][{2}]".format(pos["1"]["3"],pos["2"]["3"],pos["3"]["3"]),"\n")

def resolve(posi,turn):
    try:
        x,y = eval(posi)
    except:
        print("Invalid coordinates, try again!\n")
        if turn == "X":
            P2()
        else:
            P1()
    sym = turn
    try:
        if pos[str(x)][str(y)] in ["X","O"]:
            print("There's already a marker there!")
            display()
            if turn == "X":
                P2()
            else:
                P1()
        else:
            pos[str(x)][str(y)] = sym
            display()
    except:
        print("Coordinates outside of range! (max 3,3)\n")
        if turn == "X":
                P2()
        else:
                P1()


def P1():
    test()
    turn = "O"
    print("Give coordinates of placement, in the format of x,y")
    print("Player 1's turn!\n")
    resolve(input("> "),turn)
    P2()

def P2():
    test()
    turn = "X"
    print("Give coordinates of placement, in the format of x,y")
    print("Player 2's turn!\n")
    resolve(input("> "),turn)
    P1()

def ask():
    global pos
    global pos_clear
    print("play again? (Y/N)")
    inp = input()
    if inp.lower() == "y":
        pos = pos_clear
        clear()
        P1()
    elif inp.lower() == "n":
        sys.exit()
    else:
        print("Undefined keyword")
        ask()
menu()
