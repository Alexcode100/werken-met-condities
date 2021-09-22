#BEGIN
print('----------------------------------------------')
print('Welkom bij de:\nCircusdirecteur voor Circus HotelDeBotel Vacature')
print('----------------------------------------------')
print('Laten we beginnen!')
#BEGIN



#NAAM EN LEEFTIJD
Naam = (input('Wat is uw voor en achternaam? '))
Leeftijd = (input('Wat is uw leeftijd? '))
#NAAM EN LEEFTIJD 



#PRAKTIJK ERVARING CODE
PraktijkErvaring = (input('Hoeveel jaar praktijk ervaring heeft u met Dieren-Dressuur? '))

PraktijkErvaring2 = (input('Hoeveel jaar ervaring heeft u met jongleren? '))

PraktijkErvaring3 = (input('Hoevel jaar praktijk ervaring heeft u met acrobatiek? '))

Diploma = (input('Bent u in bezit van een Diploma MBO-4 ondernemen? (ja/nee) '))
#PRAKTIJK ERVARING CODE



#DIPLOMA CODE
Rijbewijs = (input('Bent u in bezit van een geldig Vrachtwagen rijbewijs(ja/nee) '))
#DIPLOMA CODE



#RIJBEWIJS CODE
HogeHoed = (input('Bent u in bezit van een hoge hoed?(ja/nee) '))  
#RIJBEWIJS CODE



#HOGEHOED CODE
ManVraag = (input('Bent u een (Man/Vrouw) '))
#HOGEHOED CODE



#SNORVRAAG VOOR ALS MAN
if ManVraag == "Man":
    SnorVraag = (input('Heeft u een snor? (ja/nee) '))  
    if SnorVraag == "ja":
        BreedteSnorVraag = input('Hoe breed is uw snor? ')
        if int(BreedteSnorVraag) >=10:
            Lengte = input('Hoelang bent u? ')
        else:
            Lengte = input('Hoelang bent u? ')
    else:
        Lengte = input('Hoelang bent u? ')
#SNORVRAAG VOOR ALS MAN



#KRULLHAARVRAAG VOOR ALS VROUW
else:
    Krullhaar = input('Heeft u rood krullhaar? (ja/nee) ')
    if Krullhaar == "ja":
        LengteHaar = input('Hoelang is uw haar? ')
        Lengte = input('Hoelang bent u? ')


#KRULLHAARVRAAG VOOR ALS VROUW



#GEWICHT
Gewicht = input('Hoeveel weegt u? ')
#GEWICHT



#CERTIFICAAT + GESLAAGD JA OF NEE

Certificaat = input('Heeft u de certificaat “Overleven met gevaarlijk personeel”? (ja/nee) ')

if Certificaat == "ja":
    print('---------------------------------------------\nGefeliciteerd!\nU bent aangenomen als ruimtevuilnisman!\n---------------------------------------------')
else:
    print('------------------------------\nHelaas!\nU moet de certificaat "Overleven met gevaarlijk personeel” hebben om bij ons te kunnen werken!\n---------------------------------------------')
#CERTIFICAAT + GESLAAGD JA OF NEE



















    