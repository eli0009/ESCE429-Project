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
        """Test case for /todos/:id/categories/:id"""
        r = sendRequest("DELETE", f"{self.URL}/{self.category_id}")
        self.assertEqual(len(todosCategoriesGetEntries()), 0)

    def testPost(self):
        r = sendRequest("POST", self.URL, data=TEST_DATA_CATEGORY)
        # check that there are 2 categories
        self.assertEqual(len(todosCategoriesGetEntries()), 2)
        # check that there is a new category associated with the id
        self.assertEqual(len(todosGetEntries()[0].get("categories")), 2)


if __name__ == "__main__":
    unittest.main()
    print(todosCategoriesGetEntries())
    print(todosCategoriesGetEntries()[0].get("id"))
