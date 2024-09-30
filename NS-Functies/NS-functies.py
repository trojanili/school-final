def standaardprijs(afstand_km):
    if afstand_km < 0:
        afstand_km = 0

    if afstand_km <= 50:
        prijs = afstand_km * 0.80

    else:
        prijs = 15 + (afstand_km * 0.60)
    return prijs


def ritprijs(leeftijd, weekend_rit, afstand_km):
    prijs = standaardprijs(afstand_km)
    if leeftijd < 12 or leeftijd >= 65:
        # ↑kinderen en ouderen krijgen doordeweeks 30% korting.
        if weekend_rit:
            prijs *= 0.65
        # ↑in het weekend krijgen ze ietsjes meer korting van 5%. dus in totaal 35% korting als het het weekend is.
        else:
            prijs *= 0.70
    # ↑ de groep 12 tot 64 jaar betalen de volledige standaardprijs. geen korting.
    else:
        if weekend_rit:
            prijs *= 0.60
    # ↑in het weekend krijgt deze groep meer korting? namelijk 40%
    return prijs

# int(input('hoe oud ben je?'))
