import xml.dom.minidom  # For pretty printing XML
import xml.etree.ElementTree as ET
from pprint import pprint

import requests


def printResponse(response, type):
    """
    pretty print the response differently depending on the content type
    response: response object from requests
    type(json, xml): the type of the response
    """
    if type == "json":
        pprint(response.json(), indent=4)
    elif type == "xml":
        root = ET.fromstring(response.text)
        # Pretty print the XML data
        xml_str = ET.tostring(root, encoding="utf8").decode("utf8")
        xml_str_pretty = xml.dom.minidom.parseString(xml_str).toprettyxml()
        print(xml_str_pretty)


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
    data (dict): the data to send with the request,
    payload_type (str): the type of the data to send with the request,
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
            if method == "HEAD":
                pprint(response.headers, indent=4)
            elif method in ("GET", "POST"):
                printResponse(response, payload_type)
        return response
    else:
        if prettyprint:
            print(f"{method} Error {response.status_code}: {response.reason}")
        return None
