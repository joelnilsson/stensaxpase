#importerar random och getpass samt gör variabeln loop till false
import random
import getpass
import time
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
        playerScore = 0
        compScore = 0
        antalRundor = int(input("Hur många rundor vill du spela?: "))
        antalRundor = antalRundor - 1
        while win == False:
            if rundor > antalRundor:
                if playerScore == compScore:
                    print('''
                    
                    Det blev oavgjort
                    ''', playerScore, "-", compScore, '''
                    Tack för att du spelade''')
                else:
                    print('''
                    
                    
                    Spelare har vunnit
                    ''', playerScore, "-", compScore, '''
                    Tack för att du spelade''')
                win = True
            
            else:
                time.sleep(1)
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
                    playerScore = playerScore + 1
                    rundor = rundor + 1
                elif val == 1 and datorVal == 3:
                    print('''Spelare valde sten, dator valde påse
                    dator vinner''')
                    compScore = compScore + 1
                    rundor = rundor + 1
                elif val == 2 and datorVal == 1:
                    print('''Spelare valde sax, dator valde sten
                    dator vinner''')
                    compScore = compScore + 1
                    rundor = rundor + 1
                elif val == 2 and datorVal == 3:
                    print('''Spelare valde sax, dator valde påse
                    spelare vinner''')
                    playerScore = playerScore + 1
                    rundor = rundor + 1
                elif val == 3 and datorVal == 1:
                    print('''Spelare valde påse, dator valde sten
                    spelare vinner''')
                    playerScore = playerScore + 1
                    rundor = rundor + 1
                elif val == 3 and datorVal == 2:
                    print('''Spelare valde påse, dator valde sax
                    dator vinner''')
                    compScore = compScore + 1
                    rundor = rundor + 1
#Fortsätt ange Elifs om logiken

    elif avsluta == 2:
        print("Två spelare")
        playerOneName = input("Ange namn för spelare 1: ")
        playerTwoName = input("Ange namn för spelare 2: ")
        win = False
        playerOneScore = 0
        playerTwoScore = 0
        rundor = 0
        antalRundor = int(input("Hur många rundor vill du spela?: "))
        antalRundor = antalRundor - 1
        while win == False:
            if playerOneScore > playerTwoScore:
                winner = playerOneName
            else:
                winner = playerTwoName 
            if rundor > antalRundor:
                if playerOneScore == playerTwoScore:
                    print('''
                    
                    Det blev oavgjort
                    ''', playerOneScore, "-", playerTwoScore, '''
                    Tack för att du spelade''')
                else:
                    print('''
                    
                    ''',
                    winner, '''har vunnit
                    ''', playerOneScore, "-", playerTwoScore, '''
                    Tack för att du spelade''')
                win = True
            else:
                time.sleep(1)
                print('''
                1. Sten
                2. Sax
                3. Påse
                ''')
                playerOneC = getpass.getpass("Spelare 1 väljer: ")
                playerTwoC = getpass.getpass("Spelare 2 väljer: ")
                playerOneC = int(playerOneC)
                playerTwoC = int(playerTwoC)
                if playerOneC == playerTwoC:
                    print("Ni valde samma alternativ, spela igen")
                elif playerOneC == 1 and playerTwoC == 2:
                    print('''Spelare 1 valde sten, spelare 2 valde sax
                    spelare 1 vinner''')
                    playerOneScore = playerOneScore + 1
                    rundor = rundor + 1
                elif playerOneC == 1 and playerTwoC == 3:
                    print('''Spelare 1 valde sten, spelare 2 valde påse
                    spelare 2 vinner''')
                    playerTwoScore = playerTwoScore + 1
                    rundor = rundor + 1
                elif playerOneC == 2 and playerTwoC == 1:
                    print('''Spelare 1 valde sax, spelare 2 valde sten
                    spelare 2 vinner''')
                    playerTwoScore = playerTwoScore + 1
                    rundor = rundor + 1
                elif playerOneC == 2 and playerTwoC == 3:
                    print('''Spelare 1 valde sax, spelare 2 valde påse
                    spelare 1 vinner''')
                    playerOneScore = playerOneScore + 1
                    rundor = rundor + 1
                elif playerOneC == 3 and playerTwoC == 1:
                    print('''Spelare 1 valde påse, spelare 2 valde sten
                    spelare 1 vinner''')
                    playerOneScore = playerOneScore + 1
                    rundor = rundor + 1
                elif playerOneC == 3 and playerTwoC == 2:
                    print('''Spelare 1 valde påse, spelare 2 valde sax
                    spelare 2 vinner''')
                    playerTwoScore = playerTwoScore + 1
                    rundor = rundor + 1

#gör klart spelet mot datorn innan vi fortsätter göra logiken mot en annan spelare

    elif avsluta == 3:
        exit("Tack för att du spelade")
    else:
        print("Var vänlig välj ett giltigt alternativ")

