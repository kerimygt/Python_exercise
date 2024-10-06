import requests
import csv
from fake_useragent import UserAgent
from http import HTTPStatus


def get_websites(csv_path: str) -> list[str]:
    websites: list[str] = []
    with open(csv_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if 'https://' not in row[1]:
                websites.append(f"https://{row[1]}")
            else:
                websites.append(row[1])
        return websites


def user_agent() -> str:
    ua = UserAgent()
    return ua.chrome


def get_status_description(status_code: int) -> str:
    for value in HTTPStatus:
        if value == status_code:
            description: str = f" {value} {value.name} {value.description}"
            return description
    return "Unknown status code."


def check_website(websites: str, user_agent):
    try:
        code: int = requests.get(websites, headers={'User_Agent': user_agent}).status_code
        print(websites, get_status_description(code))
    except Exception:
        print(f"Could not get information websites : {websites}")


sites: list[str] = get_websites('websites.csv')
ua: str = user_agent()
for site in sites:
    check_website(site, ua)
