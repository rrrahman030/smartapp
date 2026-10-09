import requests


def huidige_temperatuur():
    # Coördinaten van Utrecht
    latitude = 52.09
    longitude = 5.12

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&current=temperature_2m"
    )

    try:
        response = requests.get(url, timeout=10)

        data = response.json()

        temperatuur = data["current"]["temperature_2m"]

        return temperatuur

    except requests.RequestException:
        print("Er ging iets fout bij het ophalen van het weer.")
        return None

    except KeyError:
        print("De temperatuur kon niet worden gevonden.")
        return None

