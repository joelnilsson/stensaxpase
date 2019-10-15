import random
loop = False


print("Välkommen till sten, sax, påse!")

while loop = False:
    print('''
    1. Starta spel
    2. Avsluta''')
    avsluta = input("Välj alternativ")
    if avsluta == 1:
        print("Du spelar mot en dator")
        datorVal = random()
        print('''
        1. Sten
        2. Sax
        3. Påse''')
        Val = input("Välj ett alternativ")


    elif avsluta == 2:
        exit("Tack för att du spelade") 
    else:
        print("Var vänlig välj ett giltigt alternativ")

