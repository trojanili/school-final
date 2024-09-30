def aantal_kluizen_vrij():
    with open('kluizen.txt', 'r') as f:
        regel1 = f.readlines()
    gebruikte_kluizen = len(regel1)
    totale_kluizen = 12
    return totale_kluizen - gebruikte_kluizen


def nieuwe_kluis():
    vrije_kluizen = aantal_kluizen_vrij()
    if vrije_kluizen <= 0:
        return -2  # -2 staat voor geen vrije kluizen beschikbaar.
    code = input('voer een code in van min 4 tekens')
    if len(code) < 4 or ';' in code:
        return -1  # -1 staat voor ongeldige code.
    gebruikte_kluizen = []
    with open('kluizen.txt', 'r') as f:
        regel1 = f.readlines()
    for regel in regel1:
        kluisnummer = int(regel.split(';')[0])
        gebruikte_kluizen.append(kluisnummer)
    for kluisnummer in range(1, 13):
        if kluisnummer not in gebruikte_kluizen:
            with open('kluizen.txt', 'a') as f:
                f.write(f'{kluisnummer};{code}\n')
                return kluisnummer


def kluis_openen():
    kluisnummer = input('wat is de nummer van uw kluis')
    code = input('voer uw code in')
    with open('kluizen.txt', 'r') as f:
        for regel in f:
            nummer, opgeslagen_code = regel.split(';')
            if nummer == kluisnummer and opgeslagen_code == code:
                return True
    return False
