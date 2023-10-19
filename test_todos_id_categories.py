import unittest

from helper_functions import *


class TestTodosIdCategories(unittest.TestCase):
    def setUp(self):
        ## wipe all id and categories data
        self.assertTrue(todosSetUp("todos"))
        ## add entry and get id
        r = sendRequest("POST", "todos", data=TEST_DATA_ID)
        self.id = r.json().get("id")
        self.URL = f"todos/{self.id}/categories"
        ## add category and get id
        r = sendRequest("POST", self.URL, data=TEST_DATA_CATEGORY)
        self.category_id = todosCategoriesGetEntries()[0].get("id")

        # assert that there is one id and one category
        self.assertEqual(len(todosGetEntries()), 1)
        self.assertEqual(len(todosCategoriesGetEntries()), 1)

    def testXML(self):
        r = sendRequest("GET", self.URL, payload_type="xml")
        self.assertTrue(isXML(r))

    def testJSON(self):
        r = sendRequest("GET", self.URL, payload_type="json")
        self.assertTrue(isJSON(r))

    def testHead(self):
        r = sendRequest("HEAD", self.URL)
        self.assertTrue(isHEAD(r))

    def testDelete(self):
        r = sendRequest("DELETE", f"{self.URL}/{self.category_id}")
        self.assertEqual(len(todosCategoriesGetEntries()), 0)


if __name__ == "__main__":
    print(todosCategoriesGetEntries())
    print(todosCategoriesGetEntries()[0].get("id"))
