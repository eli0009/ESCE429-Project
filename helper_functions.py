import xml.dom.minidom  # For pretty printing XML
import xml.etree.ElementTree as ET
from pprint import pprint

import requests

TEST_DATA_ID = {
    "title": "officia deserunt mol",
    "doneStatus": True,
    "description": "deserunt mollit anim",
}
TEST_DATA_CATEGORY = {
    "title": "Whatever",
    "description": "This is a description",
}

TEST_DATA_TASKOF = {
    "title": "Test Taskof Title",
    "completed": False,
    "active": False,
    "description": "Test Taskof description",
}

TEST_DATA_PROJECT = {
    "title": "Test Project Title",
    "completed": False,
    "active": True,
    "description": "Test Project description",
}


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
    payload_type="json",
    base_url="http://localhost:4567/",
):
    """
    Send a request to the API and return the response
    prettyprint: if True, prettyprint the response (only for GET requests)
    data (dict): the data to send with the request,
    payload_type (str): the type of the data to send with the request,
    """
    headers = {"Accept": f"application/{payload_type}", "Content-Type": "text/plain"}

    try:
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
    except:
        return None


"""Check response is valid XML and JSON"""


def isAPIRunning(URL):
    """
    Check that the API is running
    """
    r = sendRequest("GET", URL)
    if r is None:
        return False
    else:
        return True


def isJSON(response):
    """
    Check that the response is valid JSON
    response: response object from requests
    """
    try:
        response.json()
        return True
    except ValueError:
        return False


def isXML(response):
    """
    Check that the response is valid XML
    response: response object from requests
    """
    try:
        ET.fromstring(response.text)
        return True
    except ET.ParseError:
        return False


def isHEAD(response):
    """
    Check that the response is a valid HEAD response
    """
    if (
        response.status_code == 200
        and response.text == ""
        and response.headers.get("Content-Type") == "application/json"
    ):
        return True
    else:
        return False


"""Test todos"""


def todosGetEntries(URL="todos"):
    """
    Get all entries from the todos database
    """
    r = sendRequest("GET", URL)
    return r.json().get("todos")


def todosCategoriesGetEntries(URL="todos/:id/categories"):
    r = sendRequest("GET", URL)
    return r.json().get("categories")


def todosTaskofGetEntries(URL="todos/:id/tasksof"):
    r = sendRequest("GET", URL)
    return r.json().get("projects")


def todosSetUp(URL="todos"):
    """
    SetUp database for testing, test if API is running,
    delete all data from database, including id, categories, projects
    """
    # check if api is running
    if isAPIRunning(URL) is False:
        return False

    ## delete all data database
    for entry in todosGetEntries(URL):
        sendRequest("DELETE", f"todos/{entry.get('id')}")
    # check if database is empty
    if len(todosGetEntries(URL)) != 0:
        return False

    return True

"""Test projects"""
def projectsGetEntries(URL="projects"):
    """
    Get all entries from the projects database
    """
    r = sendRequest("GET", URL)
    return r.json().get("projects")

def projectsSetUp(URL="projects"):
    """
    Remove all entries from the projects database
    """
    # check if api is running
    if isAPIRunning(URL) is False:
        return False
    
    ## delete all data database
    for entry in projectsGetEntries(URL):
        sendRequest("DELETE", f"projects/{entry.get('id')}")
    
    # check if database is empty
    if len(projectsGetEntries(URL)) != 0:
        return False
    
    return True