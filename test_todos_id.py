import unittest

from helper_functions import *


class TestTodosId(unittest.TestCase):
    def setUp(self):
        self.assertTrue(todosSetUp("todos"))
        self.data = {
            "title": "officia deserunt mol",
            "doneStatus": True,
            "description": "deserunt mollit anim",
        }
        self.r = sendRequest("POST", "todos", data=self.data)
        self.id = self.r.json().get("id")
        self.URL = f"todos/{self.id}"

    def testXML(self):
        r = sendRequest("GET", self.URL, payload_type="xml")
        self.assertTrue(isXML(r))

    def testJSON(self):
        r = sendRequest("GET", self.URL, payload_type="json")
        self.assertTrue(isJSON(r))

    def testHead(self):
        r = sendRequest("HEAD", self.URL)
        self.assertTrue(isHEAD(r))

    def testGet(self):
        self.assertEqual(todosGetEntries()[0].get("id"), self.id)

    def testDelete(self):
        r = sendRequest("DELETE", self.URL)
        self.assertEqual(len(todosGetEntries()), 0)

    def testPost(self):
        self.data["title"] = "new title"
        sendRequest("POST", self.URL, data=self.data)
        self.assertEqual(todosGetEntries()[0].get("id"), self.id)
        self.assertEqual(todosGetEntries()[0].get("title"), "new title")

    def testAmend(self):
        self.data["title"] = "new title"
        sendRequest("PUT", self.URL, data=self.data)
        self.assertEqual(todosGetEntries()[0].get("id"), self.id)
        self.assertEqual(todosGetEntries()[0].get("title"), "new title")


if __name__ == "__main__":
    data = {
        "title": "officia deserunt mol",
        "doneStatus": True,
        "description": "deserunt mollit anim",
    }
    r = sendRequest("POST", "todos", prettyprint=True, data=data)
    id = r.json().get("id")
    print(id)
