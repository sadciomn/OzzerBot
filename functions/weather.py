from bs4 import BeautifulSoup
import requests


def weather_check(city):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
    }
    res = requests.get(
        f"https://www.google.com/search?q={city} погода",
        headers=headers,
    )
    soup = BeautifulSoup(res.text, "html.parser")

    current_region = soup.find("span", class_="BBwThe").getText()
    current_weather = soup.select("#wob_tm")[0].getText()
    current_title = soup.select("#wob_dc")[0].getText()
    return (current_region, current_weather, current_title)


if __name__ == "__main__":
    city_input = input("Введите название города: ")
    print(weather_check(city_input)[2])
