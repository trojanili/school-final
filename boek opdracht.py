import math


def perimeter(straal):
    omtrek = 2 * straal * math.pi
    print(f'de omtrek van de cirkel is: {omtrek}')

straal = float(input('geef een waarde om de omtrek van een cirkel te berekenen'))

print(perimeter(straal))

# print (return)
