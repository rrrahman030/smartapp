def aantal_dagen(inputFile):
    bestand = open(inputFile, "r")
    regels = bestand.readlines()
    bestand.close()

    # Eerste regel zijn de kolomnamen
    return len(regels) - 1


def auto_bereken(inputFile, outputFile):
    bestand = open(inputFile, "r")
    regels = bestand.readlines()
    bestand.close()

    uitvoer = open(outputFile, "w")

    # Eerste regel overslaan
    for regel in regels[1:]:
        gegevens = regel.split()

        datum = gegevens[0]
        aantal_personen = int(gegevens[1])
        setpoint = float(gegevens[2])
        buitentemperatuur = float(gegevens[3])
        neerslag = float(gegevens[4])

        # CV-ketel
        verschil = setpoint - buitentemperatuur

        if verschil >= 20:
            cv_ketel = 100

        elif verschil >= 10:
            cv_ketel = 50

        else:
            cv_ketel = 0

        # Ventilatie
        ventilatie = aantal_personen + 1

        if ventilatie > 4:
            ventilatie = 4

        # Bewatering
        if neerslag < 3:
            bewatering = True

        else:
            bewatering = False

        uitvoer.write(
            datum + ";" +
            str(cv_ketel) + ";" +
            str(ventilatie) + ";" +
            str(bewatering) + "\n"
        )

    uitvoer.close()


def overwrite_settings(outputFile):
    datum = input("Welke datum wil je aanpassen? ")

    bestand = open(outputFile, "r")
    regels = bestand.readlines()
    bestand.close()

    datum_gevonden = False

    for regel in regels:
        gegevens = regel.strip().split(";")

        if gegevens[0] == datum:
            datum_gevonden = True

    if datum_gevonden == False:
        return -1

    print("1. CV-ketel")
    print("2. Ventilatie")
    print("3. Bewatering")

    systeem = input("Welk systeem wil je aanpassen? ")

    if systeem != "1" and systeem != "2" and systeem != "3":
        return -3

    try:
        waarde = int(input("Welke nieuwe waarde wil je instellen? "))
    except ValueError:
        return -3

    # Waarde controleren
    if systeem == "1":
        if waarde < 0 or waarde > 100:
            return -3

    elif systeem == "2":
        if waarde < 0 or waarde > 4:
            return -3

    elif systeem == "3":
        if waarde != 0 and waarde != 1:
            return -3

    nieuwe_regels = []

    for regel in regels:
        gegevens = regel.strip().split(";")

        if gegevens[0] == datum:

            if systeem == "1":
                gegevens[1] = str(waarde)

            elif systeem == "2":
                gegevens[2] = str(waarde)

            elif systeem == "3":
                if waarde == 0:
                    gegevens[3] = "False"
                else:
                    gegevens[3] = "True"

            nieuwe_regel = (
                gegevens[0] + ";" +
                gegevens[1] + ";" +
                gegevens[2] + ";" +
                gegevens[3] + "\n"
            )

            nieuwe_regels.append(nieuwe_regel)

        else:
            nieuwe_regels.append(regel)

    bestand = open(outputFile, "w")
    bestand.writelines(nieuwe_regels)
    bestand.close()

    return 0


def smart_app_controller():
    inputFile = "input.txt"
    outputFile = "output.txt"

    while True:
        print()
        print("===== SMART APP CONTROLLER =====")
        print("1. Aantal dagen")
        print("2. Automatisch berekenen")
        print("3. Waarde overschrijven")
        print("4. Stoppen")

        keuze = input("Maak een keuze: ")

        if keuze == "1":
            try:
                dagen = aantal_dagen(inputFile)
                print("Aantal dagen:", dagen)

            except FileNotFoundError:
                print("Het invoerbestand is niet gevonden.")

        elif keuze == "2":
            try:
                auto_bereken(inputFile, outputFile)
                print("De waarden zijn berekend.")
                print("De resultaten staan in output.txt.")

            except FileNotFoundError:
                print("Het invoerbestand is niet gevonden.")

        elif keuze == "3":
            try:
                resultaat = overwrite_settings(outputFile)

                if resultaat == 0:
                    print("De waarde is aangepast.")

                elif resultaat == -1:
                    print("Datum niet gevonden.")

                elif resultaat == -3:
                    print("Ongeldige waarde of ongeldig systeem.")

            except FileNotFoundError:
                print("Het uitvoerbestand bestaat nog niet.")

        elif keuze == "4":
            print("Programma gestopt.")
            break

        else:
            print("Ongeldige keuze.")


if __name__ == "__main__":
    smart_app_controller()