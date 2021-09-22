#Gemaakt door:
#---------
#Alexander den Otter  -  (99067410)
#Joris Lubbers  -  (99067627)
#---------

#imports
import random
import sys
import os
#imports


#Welkom
os.system('cls')
print('----------------------------------------------------------------')
print('\033[1mThe heist\033[0m')
print('----------------------------------------------------------------')
print('''Hallo! Vandaag ga jij proberen een telefoonwinkel te overvallen!\nJij gaat proberen een bepaalde waarde aan telefoons te stelen\nZWaardoor jij winst kan maken met jou overval!''')
print('----------------------------------------------------------------')
#Welkom


#Kies(Start/Regels)
StartOfRegels = input('(Typ \033[1m1\033[0m om te Starten!)\n(typ \033[1m2\033[0m voor de Uitleg!)\n---> ')
os.system('cls')
#Kies(Start/Regels)



#MoeilijkheidsKeuze1
if StartOfRegels == "1":
    Gebruikersnaam = input('\n\n\n\n\n\033[1mGebruikersnaam\033[0m: ')
    os.system('cls')
    print('----------------------------------------------------------------')
    print('Je kan nu kiezen welke moeilijkheid je wilt:')
    print('----------------------------------------------------------------')
    Moeilijkheid = input('Typ \033[1m1\033[0m voor Makkelijk\nTyp \033[1m2\033[0m voor Normaal\nTyp \033[1m3\033[0m voor Moeilijk\n---> ')
    os.system('cls')
#MoeilijkheidsKeuze1


#Uitleg
else:
    print('''--------------------------------------------------------------------------------------------------------------------------------\nJij gaat een Apple Store overvallen waarbij je gaat proberen een bepaalde waarde aan telefoons te stelen,
Je kan steeds kiezen welke telefoon je wilt stelen, alleen de vraag is welke telefoon je steelt. De goedkopere? Of de duurdere?
De keuze is aan jou. Bij een goedkope telefoon heb je minder beveiliging en dus minder kans dat het alarm afgaat als je hem steelt
Bij de duurdere telefoon heb je meer beveiliging en dus meer kans dat het alarm afgaat. En dat de politie je oppakt.\nDus wees voorzichtig en kies verstandig!\n--------------------------------------------------------------------------------------------------------------------------------''')
    
#Uitleg


#Start
    Start = input('(Typ \033[1m1\033[0m om te starten!)\n---> ')
    os.system('cls')
    Gebruikersnaam = input('\n\n\n\n\n\033[1mGebruikersnaam\033[0m: ')
    os.system('cls')
#Start


#MoeilijkheidsKeuze2
    print('----------------------------------------------------------------')
    print('Je kan nu kiezen welke moeilijkheid je wilt:')
    print('----------------------------------------------------------------')
    Moeilijkheid = input('Typ \033[1m1\033[0m voor Makkelijk\nTyp \033[1m2\033[0m voor Normaal\nTyp \033[1m3\033[0m voor Moeilijk\n---> ')
    os.system('cls')
#MoeilijkheidsKeuze2


#Bedragen1
Bedrag1 = 280
Bedrag2 = 350
Bedrag3 = 450
Bedrag4 = 900
Bedrag5 = 500
Bedrag6 = 600
Bedrag7 = 80
Bedrag8 = 150
Bedrag9 = 225
Bedrag10 = 450
Bedrag11 = 950
Bedrag12 = 1400
Bedrag13 = 550
Bedrag14 = 750
Bedrag15 = 650
Bedrag16 = 800
Bedrag17 = 950
Bedrag18 = 1350
Bedrag19 = 400
Bedrag20 = 550
totaal = 0
#Bedragen1


#Begin
if Moeilijkheid == "1":
    begrepen = input('---------------------------------------\nJe bent binnengebroken bij de Apple Shop!\nJe moet 6000$ intotaal stelen.\n---------------------------------------\nTyp \033[1mbegrepen\033[0m om verder te gaan\n---> ') 
    os.system('cls')
#Begin


#Overval1
    Easy1 = input('---------------------------------------\nJe ziet een 280$ mobiel en een 350$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 280$ mobiel\nTyp \033[1m2\033[0m voor de 350$ mobiel\n---> ')
#Overval1


#kanscode1
    chance = random.randint(1,100)
    if chance <= 4 and Easy1=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Easy1=="1":
        totaal += Bedrag1

    chance = random.randint(1,100)
    if chance <= 5 and Easy1 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Easy1=="2":
        totaal += Bedrag2
#kanscode1


#TotaalBedrag1
    os.system('cls')
    if Easy1 == "1":
        print('U heeft nu '+ str(totaal)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+ str(totaal)+'$ aan waarde gestolen! ')
#TotaalBedrag1


#Overval2
    Easy2 = input('---------------------------------------\nJe ziet een 450$ mobiel en een 900$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 450$ mobiel\nTyp \033[1m2\033[0m voor de 900$ mobiel\n---> ')
#Overval2


#kanscode2
    chance = random.randint(1,100)
    if chance <= 5 and Easy2=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Easy2 == "1":
        totaal += Bedrag3

    chance = random.randint(1,100)
    if chance <= 8 and Easy2 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Easy2 == "2":
        totaal += Bedrag4
#kanscode2


#TotaalBedraag2
    os.system('cls')
    if Easy2 == "1":
        print('U heeft nu '+str(totaal)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+str(totaal)+'$ aan waarde gestolen! ')
#TotaalBedraag2


#Overval3
    Easy3 = input('---------------------------------------\nJe ziet een 500$ mobiel en een 600$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 500$ mobiel\nTyp \033[1m2\033[0m voor de 600$ mobiel\n---> ')
#Overval3


#kanscode3
    chance = random.randint(1,100)
    if chance <= 4 and Easy3=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Easy3 == "1":
        totaal += Bedrag5

    chance = random.randint(1,100)
    if chance <= 6 and Easy3 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Easy3 == "2":
        totaal += Bedrag6
#kanscode3


#TotaalBedraag3
    os.system('cls')
    if Easy3 == "1":
        print('U heeft nu '+str(totaal)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+str(totaal)+'$ aan waarde gestolen! ')
#TotaalBedraag3


#Overval4
    Easy4 = input('---------------------------------------\nJe ziet een 80$ mobiel en een 150$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 80$ mobiel\nTyp \033[1m2\033[0m voor de 150$ mobiel\n---> ')
#Overval4


#kanscode4
    chance = random.randint(1,100)
    if chance <= 1 and Easy4=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Easy4 == "1":
        totaal += Bedrag7

    chance = random.randint(1,100)
    if chance <= 2 and Easy4 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Easy4 == "2":
        totaal += Bedrag8
#kanscode4


#TotaalBedraag4
    os.system('cls')
    if Easy4 == "1":
        print('U heeft nu '+str(totaal)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+str(totaal)+'$ aan waarde gestolen! ')
#TotaalBedraag4


#Overval5
    Easy5 = input('---------------------------------------\nJe ziet een 225$ mobiel en een 450$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 225$ mobiel\nTyp \033[1m2\033[0m voor de 450$ mobiel\n---> ')
#Overval5


#kanscode5
    chance = random.randint(1,100)
    if chance <= 3 and Easy5=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Easy5 == "1":
        totaal += Bedrag9

    chance = random.randint(1,100)
    if chance <= 5 and Easy5 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Easy5 == "2":
        totaal += Bedrag10
#kanscode5


#TotaalBedraag5
    os.system('cls')
    if Easy5 == "1":
        print('U heeft nu '+str(totaal)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+str(totaal)+'$ aan waarde gestolen! ')
#TotaalBedraag5


#Overval6
    Easy6 = input('---------------------------------------\nJe ziet een 950$ mobiel en een 1400$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 950$ mobiel\nTyp \033[1m2\033[0m voor de 1400$ mobiel\n---> ')
#Overval6


#kanscode6
    chance = random.randint(1,100)
    if chance <= 8 and Easy6=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Easy6 == "1":
        totaal += Bedrag11

    chance = random.randint(1,100)
    if chance <= 13 and Easy6 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Easy6 == "2":
        totaal += Bedrag12
#kanscode6


#TotaalBedraag6
    os.system('cls')
    if Easy6 == "1":
        print('U heeft nu '+str(totaal)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+str(totaal)+'$ aan waarde gestolen! ')
#TotaalBedraag6


#Overval7
    Easy7 = input('---------------------------------------\nJe ziet een 550$ mobiel en een 750$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 550$ mobiel\nTyp \033[1m2\033[0m voor de 750$ mobiel\n---> ')
#Overval7


#kanscode7
    chance = random.randint(1,100)
    if chance <= 4 and Easy7=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Easy7 == "1":
        totaal += Bedrag13

    chance = random.randint(1,100)
    if chance <= 9 and Easy7 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Easy7 == "2":
        totaal += Bedrag14
#kanscode7


#TotaalBedraag7
    os.system('cls')
    if Easy7 == "1":
        print('U heeft nu '+str(totaal)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+str(totaal)+'$ aan waarde gestolen! ')
#TotaalBedraag7


#Overval8
    Easy8 = input('---------------------------------------\nJe ziet een 650$ mobiel en een 800$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 650$ mobiel\nTyp \033[1m2\033[0m voor de 800$ mobiel\n---> ')
#Overval8


#kanscode8
    chance = random.randint(1,100)
    if chance <= 7 and Easy8=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Easy8 == "1":
        totaal += Bedrag15

    chance = random.randint(1,100)
    if chance <= 10 and Easy8 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Easy8 == "2":
        totaal += Bedrag16
#kanscode8


#TotaalBedraag8
    os.system('cls')
    if Easy8 == "1":
        print('U heeft nu '+str(totaal)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+str(totaal)+'$ aan waarde gestolen! ')
#TotaalBedraag8


#Overval9
    Easy9 = input('---------------------------------------\nJe ziet een 950$ mobiel en een 1350$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 350$ mobiel\nTyp \033[1m2\033[0m voor de 525$ mobiel\n---> ')
#Overval9


#kanscode9
    chance = random.randint(1,100)
    if chance <= 6 and Easy9=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Easy9 == "1":
        totaal += Bedrag17

    chance = random.randint(1,100)
    if chance <= 9 and Easy9 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Easy9 == "2":
        totaal += Bedrag18
#kanscode9


#TotaalBedraag9
    os.system('cls')
    if Easy9 == "1":
        print('U heeft nu '+str(totaal)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+str(totaal)+'$ aan waarde gestolen! ')
#TotaalBedraag9


#Overval10
    Easy10 = input('---------------------------------------\nJe ziet een 400$ mobiel en een 550$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 400$ mobiel\nTyp \033[1m2\033[0m voor de 550$ mobiel\n---> ')
#Overval10


#kanscode10
    chance = random.randint(1,100)
    if chance <= 2 and Easy10=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Easy10 == "1":
        totaal += Bedrag19

    chance = random.randint(1,100)
    if chance <= 6 and Easy10 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Easy10 == "2":
        totaal += Bedrag20
#kanscode10


#Einde1
    os.system('cls')
    if totaal >= 6000:
        print('------------------\nGoed gedaan '+ str(Gebruikersnaam)+'!\nJe hebt '+ str(totaal) +'$ aan waarde gestolen.\nJe hebt \033[1mWINST\033[0m gemaakt met de overval!\n------------------')
    else:
        print('------------------\nHelaas ' + str(Gebruikersnaam) +'...\nJe hebt ' + str(totaal)+'$ aan waarde gestolen.\nJe hebt \033[1mVERLIES\033[0m gemaakt en dus was alles voor niks!\n------------------')
#Einde1


#Nummers2
NBedrag1 = 450
NBedrag2 = 825
NBedrag3 = 650
NBedrag4 = 800
NBedrag5 = 1125
NBedrag6 = 1550
NBedrag7 = 375
NBedrag8 = 550
NBedrag9 = 250
NBedrag10 = 475
NBedrag11 = 450
NBedrag12 = 675
NBedrag13 = 750
NBedrag14 = 900
NBedrag15 = 1350
NBedrag16 = 1725
NBedrag17 = 550
NBedrag18 = 700
NBedrag19 = 475
NBedrag20 = 825
totaal1 = 0
#Nummers2




#Moeilijkheid2
if Moeilijkheid == "2":
    begrepen1 = input('---------------------------------------\nJe bent binnengebroken bij de Apple Shop!\nJe moet 7500$ intotaal stelen.\n---------------------------------------\nTyp \033[1mbegrepen\033[0m om verder te gaan\n---> ')
    os.system('cls')
#Moeilijkheid2


#Overval2
    Normal1 = input('---------------------------------------\nJe ziet een 450$ mobiel en een 825$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 450$ mobiel\nTyp \033[1m2\033[0m voor de 825$ mobiel\n---> ')
#Overval2
    
    
#kanscode1
    chance = random.randint(1,100)
    if chance <= 5 and Normal1=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal1=="1":
        totaal1 += NBedrag1

    chance = random.randint(1,100)
    if chance <= 9 and Normal1 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal1=="2":
        totaal1 += NBedrag2
#kanscode1


#TotaalBedrag1
    os.system('cls')
    if Normal1 == "1":
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
#TotaalBedrag1


#Overval2
    Normal2 = input('---------------------------------------\nJe ziet een 650$ mobiel en een 800$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 650$ mobiel\nTyp \033[1m2\033[0m voor de 800$ mobiel\n---> ')
#Overval2
    
    
#kanscode2
    chance = random.randint(1,100)
    if chance <= 6 and Normal2=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal2=="1":
        totaal1 += NBedrag3

    chance = random.randint(1,100)
    if chance <= 8 and Normal2 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal2=="2":
        totaal1 += NBedrag4
#kanscode2


#TotaalBedrag2
    os.system('cls')
    if Normal2 == "1":
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
#TotaalBedrag2


#Overval3
    Normal3 = input('---------------------------------------\nJe ziet een 1125$ mobiel en een 1550$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 1125$ mobiel\nTyp \033[1m2\033[0m voor de 1550$ mobiel\n---> ')
#Overval3
    
    
#kanscode3
    chance = random.randint(1,100)
    if chance <= 12 and Normal3=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal3=="1":
        totaal1 += NBedrag5

    chance = random.randint(1,100)
    if chance <= 17 and Normal3 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal3=="2":
        totaal1 += NBedrag6
#kanscode3


#TotaalBedrag3
    os.system('cls')
    if Normal3 == "1":
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
#TotaalBedrag3


#Overval4
    Normal4 = input('---------------------------------------\nJe ziet een 375$ mobiel en een 550$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 375$ mobiel\nTyp \033[1m2\033[0m voor de 550$ mobiel\n---> ')
#Overval4
    
    
#kanscode4
    chance = random.randint(1,100)
    if chance <= 3 and Normal4=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal4=="1":
        totaal1 += NBedrag7

    chance = random.randint(1,100)
    if chance <= 5 and Normal4 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal4=="2":
        totaal1 += NBedrag8
#kanscode4


#TotaalBedrag4
    os.system('cls')
    if Normal4 == "1":
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
#TotaalBedrag4


#Overval5
    Normal5 = input('---------------------------------------\nJe ziet een 250$ mobiel en een 475$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 250$ mobiel\nTyp \033[1m2\033[0m voor de 475$ mobiel\n---> ')
#Overval5
    
    
#kanscode5
    chance = random.randint(1,100)
    if chance <= 2 and Normal5=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal5=="1":
        totaal1 += NBedrag9

    chance = random.randint(1,100)
    if chance <= 4 and Normal5 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal5=="2":
        totaal1 += NBedrag10
#kanscode5


#TotaalBedrag5
    os.system('cls')
    if Normal5 == "1":
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
#TotaalBedrag5


#Overval6
    Normal6 = input('---------------------------------------\nJe ziet een 450$ mobiel en een 675$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 450$ mobiel\nTyp \033[1m2\033[0m voor de 675$ mobiel\n---> ')
#Overval6
    
    
#kanscode6
    chance = random.randint(1,100)
    if chance <= 4 and Normal6=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal6=="1":
        totaal1 += NBedrag11

    chance = random.randint(1,100)
    if chance <= 6 and Normal6 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal6=="2":
        totaal1 += NBedrag12
#kanscode6


#TotaalBedrag6
    os.system('cls')
    if Normal6 == "1":
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
#TotaalBedrag6


#Overval7
    Normal7 = input('---------------------------------------\nJe ziet een 750$ mobiel en een 900$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 750$ mobiel\nTyp \033[1m2\033[0m voor de 900$ mobiel\n---> ')
#Overval7
    
    
#kanscode7
    chance = random.randint(1,100)
    if chance <= 8 and Normal7=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal7=="1":
        totaal1 += NBedrag13

    chance = random.randint(1,100)
    if chance <= 10 and Normal7 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal7=="2":
        totaal1 += NBedrag14
#kanscode7


#TotaalBedrag7
    os.system('cls')
    if Normal7 == "1":
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
#TotaalBedrag8


#Overval8
    Normal8 = input('---------------------------------------\nJe ziet een 1350$ mobiel en een 1725$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 1350$ mobiel\nTyp \033[1m2\033[0m voor de 1725$ mobiel\n---> ')
#Overval8
    
    
#kanscode8
    chance = random.randint(1,100)
    if chance <= 12 and Normal8=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal8=="1":
        totaal1 += NBedrag15

    chance = random.randint(1,100)
    if chance <= 20 and Normal8 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal8=="2":
        totaal1 += NBedrag16
#kanscode8


#TotaalBedrag8
    os.system('cls')
    if Normal8 == "1":
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
#TotaalBedrag8


#Overval9
    Normal9 = input('---------------------------------------\nJe ziet een 550$ mobiel en een 700$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 475$ mobiel\nTyp \033[1m2\033[0m voor de 700$ mobiel\n---> ')
#Overval9
    
    
#kanscode9
    chance = random.randint(1,100)
    if chance <= 5 and Normal9=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal9=="1":
        totaal1 += NBedrag17

    chance = random.randint(1,100)
    if chance <= 7 and Normal9 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal9=="2":
        totaal1 += NBedrag18
#kanscode9


#TotaalBedrag9
    os.system('cls')
    if Normal9 == "1":
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
#TotaalBedrag9


#Overval10
    Normal10 = input('---------------------------------------\nJe ziet een 475$ mobiel en een 825$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 475$ mobiel\nTyp \033[1m2\033[0m voor de 825$ mobiel\n---> ')
#Overval10
    
    
#kanscode10
    chance = random.randint(1,100)
    if chance <= 4 and Normal10=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal10=="1":
        totaal1 += NBedrag19

    chance = random.randint(1,100)
    if chance <= 8 and Normal10 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal10=="2":
        totaal1 += NBedrag20
#kanscode10


#Einde2
    os.system('cls')
    if totaal1 >= 7500:
        print('------------------\nGoed gedaan '+ str(Gebruikersnaam)+'!\nJe hebt '+ str(totaal1) +'$ aan waarde gestolen.\nJe hebt \033[1mWINST\033[0m gemaakt met de overval!\n------------------')
    else:
        print('------------------\nHelaas ' + str(Gebruikersnaam) +'...\nJe hebt ' + str(totaal1)+'$ aan waarde gestolen.\nJe hebt \033[1mVERLIES\033[0m gemaakt en dus was alles voor niks!\n------------------')
#Einde2




#nummers3
HBedrag1 = 725
HBedrag2 = 950
HBedrag3 = 925
HBedrag4 = 1175
HBedrag5 = 625
HBedrag6 = 850
HBedrag7 = 575
HBedrag8 = 750
HBedrag9 = 950
HBedrag10 = 1225
HBedrag11 = 625
HBedrag12 = 850
HBedrag13 = 1100
HBedrag14 = 1425
HBedrag15 = 225
HBedrag16 = 400
HBedrag17 = 425
HBedrag18 = 600
HBedrag19 = 600
HBedrag20 = 1300
totaal2 = 0
#nummers3




#Moeilijkheid3
if Moeilijkheid == "3":
    begrepen1 = input('---------------------------------------\nJe bent binnengebroken bij de Apple Shop!\nJe moet 8750$ intotaal stelen.\n---------------------------------------\nTyp \033[1mbegrepen\033[0m om verder te gaan\n---> ')
    os.system('cls')
#Moeilijkheid3


#Overval3
    Hard1 = input('---------------------------------------\nJe ziet een 725$ mobiel en een 950$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 725$ mobiel\nTyp \033[1m2\033[0m voor de 950$ mobiel\n---> ')
#Overval3
    
    
#kanscode1
    chance = random.randint(1,100)
    if chance <= 10 and Hard1=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Hard1=="1":
        totaal2 += HBedrag1

    chance = random.randint(1,100)
    if chance <= 15 and Hard1 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Hard1=="2":
        totaal2 += HBedrag2
#kanscode1


#TotaalBedrag1
    os.system('cls')
    if Hard1 == "1":
        print('U heeft nu '+ str(totaal2)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+ str(totaal2)+'$ aan waarde gestolen! ')
#TotaalBedrag1


#Overval2
    Hard2 = input('---------------------------------------\nJe ziet een 925$ mobiel en een 1175$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 925$ mobiel\nTyp \033[1m2\033[0m voor de 1175$ mobiel\n---> ')
#Overval2
    
    
#kanscode2
    chance = random.randint(1,100)
    if chance <= 15 and Hard2=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Hard2=="1":
        totaal2 += HBedrag3

    chance = random.randint(1,100)
    if chance <= 19 and Hard2 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Hard2=="2":
        totaal2 += HBedrag4
#kanscode2


#TotaalBedrag2
    os.system('cls')
    if Hard2 == "1":
        print('U heeft nu '+ str(totaal2)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+ str(totaal2)+'$ aan waarde gestolen! ')
#TotaalBedrag2


#Overval3
    Hard3 = input('---------------------------------------\nJe ziet een 625$ mobiel en een 850$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 625$ mobiel\nTyp \033[1m2\033[0m voor de 850$ mobiel\n---> ')
#Overval3
    
    
#kanscode3
    chance = random.randint(1,100)
    if chance <= 7 and Hard3=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Hard3=="1":
        totaal2 += HBedrag5

    chance = random.randint(1,100)
    if chance <= 9 and Hard3 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Hard3=="2":
        totaal2 += HBedrag6
#kanscode3


#TotaalBedrag3
    os.system('cls')
    if Hard3 == "1":
        print('U heeft nu '+ str(totaal2)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+ str(totaal2)+'$ aan waarde gestolen! ')
#TotaalBedrag3


#Overval4
    Hard4 = input('---------------------------------------\nJe ziet een 575$ mobiel en een 750$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 575$ mobiel\nTyp \033[1m2\033[0m voor de 750$ mobiel\n---> ')
#Overval4
    
    
#kanscode4
    chance = random.randint(1,100)
    if chance <= 6 and Hard4=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Hard4=="1":
        totaal2 += HBedrag7

    chance = random.randint(1,100)
    if chance <= 8 and Hard4 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Hard4=="2":
        totaal2 += HBedrag8
#kanscode4


#TotaalBedrag4
    os.system('cls')
    if Hard4 == "1":
        print('U heeft nu '+ str(totaal2)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+ str(totaal2)+'$ aan waarde gestolen! ')
#TotaalBedrag4


#Overval5
    Hard5 = input('---------------------------------------\nJe ziet een 950$ mobiel en een 1225$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 950$ mobiel\nTyp \033[1m2\033[0m voor de 1225$ mobiel\n---> ')
#Overval5
    
    
#kanscode5
    chance = random.randint(1,100)
    if chance <= 15 and Hard5=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Hard5=="1":
        totaal2 += HBedrag9

    chance = random.randint(1,100)
    if chance <= 20 and Hard5 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Hard5=="2":
        totaal2 += HBedrag10
#kanscode5


#TotaalBedrag5
    os.system('cls')
    if Hard5 == "1":
        print('U heeft nu '+ str(totaal2)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+ str(totaal2)+'$ aan waarde gestolen! ')
#TotaalBedrag5


#Overval6
    Hard6 = input('---------------------------------------\nJe ziet een 625$ mobiel en een 850$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 625$ mobiel\nTyp \033[1m2\033[0m voor de 850$ mobiel\n---> ')
#Overval6
    
    
#kanscode6
    chance = random.randint(1,100)
    if chance <= 7 and Hard6=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Hard6=="1":
        totaal2 += HBedrag11

    chance = random.randint(1,100)
    if chance <= 9 and Hard6 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Hard6=="2":
        totaal2 += HBedrag12
#kanscode6


#TotaalBedrag6
    os.system('cls')
    if Hard6 == "1":
        print('U heeft nu '+ str(totaal2)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+ str(totaal2)+'$ aan waarde gestolen! ')
#TotaalBedrag6


#Overval7
    Hard7 = input('---------------------------------------\nJe ziet een 1100$ mobiel en een 1425$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 1100$ mobiel\nTyp \033[1m2\033[0m voor de 1425$ mobiel\n---> ')
#Overval7
    
    
#kanscode7
    chance = random.randint(1,100)
    if chance <= 18 and Hard7=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Hard7=="1":
        totaal2 += HBedrag13

    chance = random.randint(1,100)
    if chance <= 25 and Hard7 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Hard7=="2":
        totaal2 += HBedrag14
#kanscode7


#TotaalBedrag7
    os.system('cls')
    if Hard7 == "1":
        print('U heeft nu '+ str(totaal2)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+ str(totaal2)+'$ aan waarde gestolen! ')
#TotaalBedrag7


#Overval8
    Hard8 = input('---------------------------------------\nJe ziet een 225$ mobiel en een 400$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 225$ mobiel\nTyp \033[1m2\033[0m voor de 400$ mobiel\n---> ')
#Overval8
    
    
#kanscode8
    chance = random.randint(1,100)
    if chance <= 3 and Hard8=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Hard8=="1":
        totaal2 += HBedrag15

    chance = random.randint(1,100)
    if chance <= 5 and Hard8 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Hard8=="2":
        totaal2 += HBedrag16
#kanscode8


#TotaalBedrag8
    os.system('cls')
    if Hard8 == "1":
        print('U heeft nu '+ str(totaal2)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+ str(totaal2)+'$ aan waarde gestolen! ')
#TotaalBedrag8


#Overval9
    Hard9 = input('---------------------------------------\nJe ziet een 425$ mobiel en een 600$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 425$ mobiel\nTyp \033[1m2\033[0m voor de 600$ mobiel\n---> ')
#Overval9
    
    
#kanscode9
    chance = random.randint(1,100)
    if chance <= 5 and Hard9=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Hard9=="1":
        totaal2 += HBedrag17

    chance = random.randint(1,100)
    if chance <= 7 and Hard9 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Hard9=="2":
        totaal2 += HBedrag18
#kanscode8


#TotaalBedrag9
    os.system('cls')
    if Hard9 == "1":
        print('U heeft nu '+ str(totaal2)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+ str(totaal2)+'$ aan waarde gestolen! ')
#TotaalBedrag9


#Overval10
    Hard10 = input('---------------------------------------\nJe ziet een 600$ mobiel en een 1300$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 600$ mobiel\nTyp \033[1m2\033[0m voor de 1300$ mobiel\n---> ')
#Overval10
    
    
#kanscode10
    chance = random.randint(1,100)
    if chance <= 5 and Hard10=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Hard10=="1":
        totaal2 += HBedrag19

    chance = random.randint(1,100)
    if chance <= 22 and Hard10 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Hard10=="2":
        totaal2 += HBedrag20
#kanscode10


#Einde3
    os.system('cls')
    if totaal2 >= 8750:
        print('------------------\nGoed gedaan '+ str(Gebruikersnaam)+'!\nJe hebt '+ str(totaal2) +'$ aan waarde gestolen.\nJe hebt \033[1mWINST\033[0m gemaakt met de overval!\n------------------')
    else:
        print('------------------\nHelaas ' + str(Gebruikersnaam) +'...\nJe hebt ' + str(totaal2)+'$ aan waarde gestolen.\nJe hebt \033[1mVERLIES\033[0m gemaakt en dus was alles voor niks!\n------------------')
#Einde3