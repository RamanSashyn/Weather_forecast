import requests


def get_weather(city_url, params=None):
    response = requests.get(city_url, params=params)
    response.raise_for_status()
    return response.text


def main():
    base_url = "https://wttr.in"
    cities = [
        ("london", None),
        ("svo", None),
        ("Череповец", {"m": "", "M": "", "n": "", "q": "", "T": "", "lang": "ru"})
    ]

    for city, params in cities:
        city_url = f"{base_url}/{city}"
        city_weather = get_weather(city_url, params)
        print(city_weather)


if __name__ == "__main__":
    main()
