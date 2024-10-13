import json
from datetime import datetime

def load_dagboek(bestandsnaam):
    try:
        with open(bestandsnaam, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_dagboek(bestandsnaam, dagboek):
    with open(bestandsnaam, 'w') as file:
        json.dump(dagboek, file, ensure_ascii=False, indent=4)

def check_datum(dagboek, datum):
    return datum in dagboek

def is_geldige_datum(datum):
    if datum.lower() == 'vandaag':
        return True
    try:
        datetime.strptime(datum, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def voeg_invoer_toe(dagboek, datum):
    if check_datum(dagboek, datum):
        while True:
            keuze = input("Wil je de tekst herschrijven (h) of toevoegen aan de bestaande tekst (a)? ").lower()
            if keuze == 'h':
                tekst = input("Voer de nieuwe tekst in: ")
                dagboek[datum] = tekst
                break
            elif keuze == 'a':
                tekst = input("Voer de tekst in die je wilt toevoegen: ")
                dagboek[datum] += "\n" + tekst
                break
            else:
                print("Ongeldige keuze. Typ 'h' om te herschrijven of 'a' om toe te voegen.")
    else:
        tekst = input("Voer de tekst in voor deze datum: ")
        dagboek[datum] = tekst

def main():
    bestandsnaam = 'dagboek.json'
    dagboek = load_dagboek(bestandsnaam)

    while True:
        datum = input("Voor welke datum wil je een invoer maken? (gebruik JJJJ-MM-DD of typ 'vandaag' voor vandaag): ")
        if is_geldige_datum(datum):
            if datum.lower() == 'vandaag':
                datum = datetime.now().strftime("%Y-%m-%d")
            break
        else:
            print("Ongeldige datum. Zorg ervoor dat het in het juiste formaat is (JJJJ-MM-DD) of typ 'vandaag'.")

    voeg_invoer_toe(dagboek, datum)
    save_dagboek(bestandsnaam, dagboek)
    print("De tekst is opgeslagen!")

if __name__ == "__main__":
    main()
