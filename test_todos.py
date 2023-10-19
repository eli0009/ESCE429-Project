import json
import unittest

from helper_functions import *


class TestTodos(unittest.TestCase):
    """Test /todos"""

    def setUp(self):
        """initialize database for testing"""
        self.URL = "todos"
        self.assertTrue(todosSetUp(self.URL))

    def testXML(self):
        r = sendRequest("GET", self.URL, payload_type="xml")
        self.assertTrue(isXML(r))

    def testJSON(self):
        r = sendRequest("GET", self.URL, payload_type="json")
        self.assertTrue(isJSON(r))

    def testAddEntry(self):
        r = sendRequest("POST", self.URL, data=TEST_DATA_ID)
        # check request success
        self.assertIsNotNone(r)
        # check data was added
        self.assertEqual(len(todosGetEntries(self.URL)), 1)

    def testGetAll(self):
        """add 5 entries and get them all"""
        for i in range(5):
            sendRequest("POST", self.URL, data=TEST_DATA_ID)
        self.assertEqual(len(todosGetEntries(self.URL)), 5)

    def testHead(self):
        r = sendRequest("HEAD", self.URL)
        self.assertTrue(isHEAD(r))


if __name__ == "__main__":
    # get
    r = sendRequest("GET", "todos", True)
    # entries = r.json().get("todos")
    # for entry in entries:
    #     sendRequest("DELETE", f"todos/{entry.get('id')}", True)

    # head
    r = sendRequest("HEAD", "todos", True)
    print(r.text == "")

    ## post
    # data = {
    #     "title": "officia deserunt mol",
    #     "doneStatus": True,
    #     "description": "deserunt mollit anim",
    # }
    # r = sendRequest(
    #     "POST",
    #     "todos",
    #     True,
    #     data,
    # )
