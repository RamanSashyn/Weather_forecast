import requests


def city_weather(city_url):
    response = requests.get(city_url)
    response.raise_for_status()
    return response.text


def main():
    london_url = "https://wttr.in/london"
    sheremetyevo_url = "https://wttr.in/svo"
    cherepovets_url = "https://wttr.in/%D0%A7%D0%B5%D1%80%D0%B5%D0%BF%D0%BE%D0%B2%D1%86%D0%B0?m&M&n&q&T&lang=ru"

    london_weather = city_weather(london_url)
    sheremety_weather = city_weather(sheremetyevo_url)
    cherepovets_weather = city_weather(cherepovets_url)

    print(london_weather)
    print(sheremety_weather)
    print(cherepovets_weather)


if __name__ == "__main__":
    main()
