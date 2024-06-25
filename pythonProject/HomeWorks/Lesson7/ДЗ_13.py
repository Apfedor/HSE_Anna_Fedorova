import requests
from datetime import datetime
from bs4 import BeautifulSoup


class CBRParser:
    
    BASE_URL = "https://www.cbr.ru"

    def __init__(self):
        self.data = None
        self.soup = None

    def get_cbr_page_soup(self, from_date: str, to_date: str):
        params = f"?UniDbQuery.Posted=True" \
                 f"&UniDbQuery.From={from_date}" \
                 f"&UniDbQuery.To={to_date}"
        url = f"{self.BASE_URL}/hd_base/KeyRate/{params}"
        r = requests.get(url)
        r.raise_for_status()
        self.soup = BeautifulSoup(r.text, 'html.parser')
        return

    def parse_cbr_data(self, soup: BeautifulSoup):
        self.data = {}
        table_cells = self.soup.find('table').find_all('td')
        dates = [d.text for i, d in enumerate(table_cells) if i % 2 == 0]
        rates = [r.text for i, r in enumerate(table_cells) if i % 2 != 0]
        self.data = list(zip(dates, rates))
        return

    def start(self):
        self.parse_cbr_data(self.get_cbr_page_soup('17.09.2013', datetime.now()))
        print(self.data)

def main():
    parser = CBRParser()
    parser.start()
    pass


if __name__ == '__main__':
    main()
