def Fahrenheit(temp_celcius):
    return 32 + 1.8 * temp_celcius


def gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid):
    return temp_celcius - luchtvochtigheid / 100 * windsnelheid


def weerrapport(temp_celcius, windsnelheid, luchtvochtigheid):
    gevoel = gevoelstemperatuur(
        temp_celcius,
        windsnelheid,
        luchtvochtigheid
    )

    if gevoel < 0 and windsnelheid > 10:
        return "Het is heel koud en het stormt! Verwarming helemaal aan!"

    elif gevoel < 0 and windsnelheid <= 10:
        return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"

    elif 0 <= gevoel < 10 and windsnelheid > 12:
        return "Het is best koud en het waait; verwarming aan en roosters dicht!"

    elif 0 <= gevoel < 10 and windsnelheid <= 12:
        return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"

    elif 10 <= gevoel < 22:
        return "Heerlijk weer, niet te koud of te warm."

    else:
        return "Warm! Airco aan!"


def weerstation():
    totale_temperatuur = 0
    aantal_dagen = 0

    for dag in range(1, 8):

        temperatuur = input(
            f"Wat is op dag {dag} de temperatuur[C]: "
        )

        if temperatuur == "":
            print("bye")
            return

        temperatuur = float(temperatuur)

        windsnelheid = input(
            f"Wat is op dag {dag} de windsnelheid[m/s]: "
        )

        if windsnelheid == "":
            print("bye")
            return

        windsnelheid = float(windsnelheid)

        luchtvochtigheid = input(
            f"Wat is op dag {dag} de vochtigheid[%]: "
        )

        if luchtvochtigheid == "":
            print("bye")
            return

        luchtvochtigheid = int(luchtvochtigheid)

        # Fahrenheit berekenen
        fahrenheit = Fahrenheit(temperatuur)

        # Gemiddelde berekenen
        totale_temperatuur = totale_temperatuur + temperatuur
        aantal_dagen = aantal_dagen + 1

        gemiddelde = totale_temperatuur / aantal_dagen

        # Resultaat printen
        print(f"Het is {temperatuur}C ({fahrenheit}F)")

        print(
            weerrapport(
                temperatuur,
                windsnelheid,
                luchtvochtigheid
            )
        )

        print(f"Gem. temp tot nu toe is {gemiddelde}")
        print("======================================")

if __name__ == "__main__":
    weerstation()