import random
import getpass
loop = False


print("Välkommen till sten, sax, påse!")

while loop == False:
    print('''
    1. Spela ensam
    2. Spela med någon
    3. Avsluta''')
    avsluta = int(input("Välj alternativ: "))
    if avsluta == 1:
        print("Du spelar mot en dator")
        datorVal = random.random(1,3)
        print('''
        1. Sten
        2. Sax
        3. Påse''')
        Val = input("Välj ett alternativ")
    elif avsluta == 2:
        print("Två spelare")
        playerOneName = input("Ange namn för spelare 1")
        playerTwoName = input("Ange namn för spelare 2")
        print('''
        1. Sten
        2. Sax
        3. Påse''')
        playerOneC = getpass.getpass(playerOneName, " väljer: ")
        playerTwoC = getpass.getpass(playerTwoName, " väljer: ")

    elif avsluta == 3:
        exit("Tack för att du spelade") 
    else:
        print("Var vänlig välj ett giltigt alternativ")

