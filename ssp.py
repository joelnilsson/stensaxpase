import random
import getpass
loop = False


print("Välkommen till sten, sax, påse!")

while loop == False:
    print('''
    1. Spela ensam
    2. Spela med någon
    3. Avsluta''')
    try:
         avsluta = int(input("Välj alternativ: "))
         
    except (ValueError):
        avsluta = 4
    if avsluta == 1:
        print("Du spelar mot en dator")
        while win == False:
            
            datorVal = random.randint(1,3)
            print('''
            1. Sten
            2. Sax
            3. Påse''')
            Val = input("Välj ett alternativ")
            if val == datorVal:
                print("Ni valde samma alternativ, spela igen")
            elif val == 1 and 
        
    elif avsluta == 2:
        print("Två spelare")
        playerOneName = input("Ange namn för spelare 1")
        playerTwoName = input("Ange namn för spelare 2")
        print('''
        1. Sten
        2. Sax
        3. Påse''')
        playerOneC = getpass.getpass("Spelare 1 väljer: ")
        playerTwoC = getpass.getpass("Spelare 2 väljer: ")

    elif avsluta == 3:
        exit("Tack för att du spelade") 
    else:
        print("Var vänlig välj ett giltigt alternativ")

