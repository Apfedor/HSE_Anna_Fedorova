import requests
from bs4 import BeautifulSoup

manager = '263411857320'
token = '4123saedfasedsadf4324234f223ddf23'


class LegalAPI:
    BASE_URL = 'https://legal-api.sirotinsky.com'

    def __init__(self, token):
        self.token = token

    def efrsb_traders_all(self):
        url = f"{self.BASE_URL}/{self.token}/efrsb/trader/all"
        r = requests.get(url)
        r.raise_for_status()
        return r.json()


def main():
    api = LegalAPI(token)
    traders = api.efrsb_traders_all()
    print('stop')


if __name__ == '__main__':
    main()
