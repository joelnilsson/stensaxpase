#importerar random och getpass samt gör variabeln loop till false
import random
import getpass
loop = False


print("Välkommen till sten, sax, påse!")
#game loop
while loop == False:
    print('''
    1. Spela ensam
    2. Spela med någon
    3. Avsluta''')
    try:
        avsluta = int(input("Välj alternativ: ")) #byt namn på variabeln
         
    except (ValueError):
        avsluta = 4
    if avsluta == 1:
        print("Du spelar mot en dator")
        rundor = 0
        win = False
        while win == False:
            if rundor > 3:
                win = True
            datorVal = random.randint(1,3)
            print('''
            1. Sten
            2. Sax
            3. Påse''')
            val = int(input("Välj ett alternativ: "))
            if val == datorVal:
                print("Ni valde samma alternativ, spela igen")
            elif val == 1 and datorVal == 2:
                print('''Spelare valde sten, dator valde sax
                spelare vinner''')
                rundor = rundor + 1
            elif val == 1 and datorVal == 3:
                print('''Spelare valde sten, dator valde påse
                dator vinner''')
                rundor = rundor + 1
            elif val == 2 and datorVal == 1:
                print('''Spelare valde sax, dator valde sten
                dator vinner''')
                rundor = rundor + 1
            elif val == 2 and datorVal == 3:
                print('''Spelare valde sax, dator valde påse
                spelare vinner''')
                rundor = rundor + 1
            elif val == 3 and datorVal == 1:
                print('''Spelare valde påse, dator valde sten
                spelare vinner''')
                rundor = rundor + 1
            elif val == 3 and datorVal == 2:
                print('''Spelare valde påse, dator valde sax
                dator vinner''')
                rundor = rundor + 1
#Fortsätt ange Elifs om logiken

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

#gör klart spelet mot datorn innan vi fortsätter göra logiken mot en annan spelare

    elif avsluta == 3:
        exit("Tack för att du spelade")
    else:
        print("Var vänlig välj ett giltigt alternativ")

