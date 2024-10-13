import random

maxGetal = 200
getal = random.randint(1, maxGetal)
pogingen = 8


def gokken():
    for poging in range(pogingen):
        while True:
            try:
                gok = int(input(f'poging {poging + 1}: raad het nummer: '))
                break
            except ValueError:
                print("Ongeldige invoer. Voer alstublieft een getal in.")

        if gok == getal:
            print('Wauw!!, Goed gedaan, je hebt het geraden!')
            break
        elif gok < getal:
            print('Het getal is hoger.')
        elif gok > getal:
            print('Het getal is lager.')

    print('helaas, volgende keer beter!')


while True:
    print('Denk jij dat je het nummer kan raden binnen', pogingen, 'pogingen? Kom maar op!')
    print('Je moet een getal raden tussen 1 tot en met', maxGetal)
    print('psstt, ik zal je een beetje helpen')
    gokken()

    opnieuw_spelen = input("Durf je het nog een keer te proberen? (ja of nee): ").lower()
    if opnieuw_spelen == 'nee':
        print("tot de volgende keer!")
        break

