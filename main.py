from weerstation import weerstation
from smart_app_controller import smart_app_controller
from weer_api import huidige_temperatuur


def hoofdmenu():
    while True:
        print()
        print("===================================")
        print("          SMART HOME HUB")
        print("===================================")
        print("1. Weerstation")
        print("2. Smart App Controller")
        print("3. Huidige temperatuur Utrecht")
        print("4. Stoppen")
        print("===================================")

        try:
            keuze = int(input("Maak een keuze: "))

            if keuze == 1:
                weerstation()

            elif keuze == 2:
                smart_app_controller()

            elif keuze == 3:
                temperatuur = huidige_temperatuur()

                if temperatuur is not None:
                    print(
                        f"De huidige temperatuur in Utrecht "
                        f"is {temperatuur} graden Celsius."
                    )

            elif keuze == 4:
                print("Programma gestopt.")
                break

            else:
                print("Kies een getal van 1 tot en met 4.")

        except ValueError:
            print("Ongeldige invoer. Vul een getal in.")


if __name__ == "__main__":
    hoofdmenu()