from zcname import constants

from requests import get


class AppRestClient:
    """ Manages the REST requests to the random user API. """
    def __init__(self):
        self.url = constants.RANDOM_USER_API_URL

    def get_full_name(self):
        """ Returns a full name, including title. """
        response = get(self.url)
        resp = response.json()["results"][0]["name"]
        return f'{resp["title"]} {resp["first"]} {resp["last"]}'


def print_full_name():
    print(AppRestClient().get_full_name())


if __name__ == '__main__':
    print_full_name()
