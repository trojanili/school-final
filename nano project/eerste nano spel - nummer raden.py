import random

maxGetal = 200
getal = random.randint(1, maxGetal)
pogingen = 8


def gokken():
    for poging in range(pogingen):
        gok = int(input(f'poging {poging + 1}: raad het nummer: '))
        if gok == getal:
            print('Wauw!!, Goed gedaan, je hebt het geraden!')
            break
        elif gok < getal:
            print('Het getal is hoger.')
        elif gok > getal:
            print('Het getal is lager.')
    print('helaas, volgende keer beter!')


while True:
    print('Denk jij dat je het nummer kan raden binnen', pogingen, 'pogingen? kom maar op!')
    print('je moet een getal raden tussen 1 tot en met', maxGetal)
    print('psstt, ik zal je een beetje helpen')
    gokken()

# durf je het nog keer te proberen 'ja' of 'nee'
# menu met moeilijkheidsgraad
