import constants

from requests import get


class AppRestClient:
    """ Manages the REST requests to the random user API """
    def __init__(self):
        self.url = constants.RANDOM_USER_API_URL

    def get_full_name(self):
        response = get(self.url)
        resp = response.json()["results"][0]["name"]
        return f'{resp["title"]} {resp["first"]} {resp["last"]}'


if __name__ == '__main__':
    print(AppRestClient().get_full_name())