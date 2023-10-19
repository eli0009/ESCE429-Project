from pprint import pprint
import requests

def sendRequest(
    method,
    url,
    prettyprint=False,
    data=None,
    base_url="http://localhost:4567/",
    headers={"Content-Type": "text/plain"},
):
    """
    Send a request to the API and return the response
    prettyprint: if True, prettyprint the response (only for GET requests)
    """
    response = requests.request(
        method,
        base_url + url,
        data=str(data),
        headers=headers,
    )

    if response.status_code in (200, 201, 204):
        if prettyprint:
            if method == "GET":
                pprint(response.json(), indent=4)
            elif method == "HEAD":
                pprint(response.headers, indent=4)
            elif method == "POST":
                pprint(response.json(), indent=4)
        return response
    else:
        if prettyprint:
            print(f"{method} Error {response.status_code}: {response.reason}")
        return None
