from pprint import pprint
import requests

def sendRequest(
    method,
    url,
    prettyprint=False,
    data=None,
):
    """
    Send a request to the API and return the response
    prettyprint: if True, prettyprint the response (only for GET requests)
    """
    response = requests.request(method, url, data=data)

    if response.status_code == 200:
        if prettyprint:
            if method == "GET":
                pprint(response.json(), indent=4)
            if method == "HEAD":
                pprint(response.headers, indent=4)
        return response
    else:
        if prettyprint:
            print(f"{method} Error {response.status_code}: {response.reason}")
        return None
