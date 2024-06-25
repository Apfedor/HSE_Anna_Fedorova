import requests

manager = '263411857320'
token = '4123saedfasedfsadf4324234f223ddf23'
inn_test = '3662086277'
endpoints: list = ["/efrsb/publisher_messages",
                   "/efrsb/debtor_messages",
                   "/efrsb/manager/all",
                   "/efrsb/manager",
                   "/efrsb/trader/all",
                   "/efrsb/trader",
                   "/efrsb/person",
                   "/efrsb/organisation"]


class LegalAPI:
    BASE_URL = 'https://legal-api.sirotinsky.com'

    def __init__(self, token):
        self.token = token

    def get(self, endpoint, inn):
        if endpoint.find('all') > 0:
            url = f"{self.BASE_URL}/{self.token}/{endpoint}"
        else:
            url = f"{self.BASE_URL}/{self.token}/{endpoint}/{inn}"

        r = requests.get(url)
        r.raise_for_status()
        return r.json()


def main():
    api = LegalAPI(token)
    traders = api.get(endpoints[4], inn_test)
    print('stop')


if __name__ == '__main__':
    main()
