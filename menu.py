from dagboek import main as dagboek_main  # Importeer de main functie van het dagboek
from nummer_raden import gokken            # Importeer de gokken functie van het spel

def main():
    while True:
        print("\n--- Hoofdmenu ---")
        print("Typ 'dagboek' om het dagboek te openen")
        print("Typ 'nummer_raden' om het nummer raden spel te spelen")
        print("Typ 'break' om het programma af te sluiten")

        keuze = input("Kies een optie: ").lower()  # Maak de invoer hoofdlettergevoelig

        if keuze == 'dagboek':
            dagboek_main()  # Start de dagboekfunctie
        elif keuze == 'nummer_raden':
            gokken()  # Start het nummer raden spel
        elif keuze == 'break':
            print("Programma wordt afgesloten.")
            break
        else:
            print("Ongeldige keuze, probeer opnieuw.")

if __name__ == "__main__":
    main()
