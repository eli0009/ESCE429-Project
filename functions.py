import requests


def sendRequest(method, url):
    """
    Send a request to the API and return the response
    """
    response = requests.request(method, url)
    if response.status_code == 200:
        return response.json()
    else:
        return None