#Alexander den Otter  -  99067410

geel = input('Is de kaas geel? ')
if geel == "ja":
    gaten = input("Zitten er gaten in? ")
    if gaten == "ja":
        duur = input("Is de kaas belachelijk duur? ")
        if duur == "ja":
            print("De kaas is Emmenthaler")
        elif duur == 'nee':
            print("De kaas is Leerdammer")
    elif gaten == "nee":
        hard = input("Is de kaas hard als steen? ")
        if hard == "ja":
            print("De kaas is Pammigiano Reggiano")
        elif hard == 'nee':
            print('De kaas is Goudse kaas')
elif geel == "nee":
    schimmel = input("Heeft de kaas Blauwe schimmels? ")
    if schimmel == "ja":
        korst = input("Heeft de kaas een korst? ")
        if korst == "ja":
            print("De kaas is Bleu de Rochbaron")
        elif korst == 'nee':
            print('de kaas is Foumme d Ambert')
    elif schimmel == 'nee':
        korst = input("Heeft de kaas een korst? ")
        if korst == "ja":
            print("De kaas is Bleu de Camembert")
        elif korst == 'nee':
            print('de kaas is Foumme d Mozzerella')