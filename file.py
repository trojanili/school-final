def nieuwe_box(naam):
    file = open(f'{naam}.txt', 'w')
    file.write('0.0')
    file.close()


def leeg_box(naam):
    with open(f'{naam}.txt', 'r') as file:
        inhoud = file.read().strip()


print(f'huidig bedrag:{inhoud}')
try:
    bedrag = float(inhoud)
    print(f'EUR {bedrag:.2f}')
except ValueError:
    print('Ongeldige inhoud in bestand')
    with open(f'{naam}.txt', 'w') as file:

def euro(naam):
    pass


def tientje(naam):
    pass


def meer_dan(naam):
    pass
