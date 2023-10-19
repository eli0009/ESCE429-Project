from pprint import pprint

import requests


def sendRequest(
    method,
    url,
    prettyprint=False,
    data=None,
    payload_type="xml",
    base_url="http://localhost:4567/",
):
    """
    Send a request to the API and return the response
    prettyprint: if True, prettyprint the response (only for GET requests)
    """
    headers = {"Accept": f"application/{payload_type}", "Content-Type": "text/plain"}

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
                pprint(response.content, indent=4)
        return response
    else:
        if prettyprint:
            print(f"{method} Error {response.status_code}: {response.reason}")
        return None
