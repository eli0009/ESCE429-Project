import unittest

from helper_functions import *


class TestProjectsCategories(unittest.TestCase):

    def setUp(self):
        self.URL = "projects"
        self.assertTrue(projectsSetUp("projects"))
        # add entry and get id
        r = sendRequest("POST", "projects", data=TEST_DATA_PROJECT)
        self.id = r.json().get("id")
        self.URL = f"projects/{self.id}/categories"
        # add category and get id
        r = sendRequest("POST", self.URL, data=TEST_DATA_PROJECT_CATEGORY)
        self.category_id = projectsCategoriesGetEntries()[0].get("id")

        # assert that there is one id and one category
        self.assertEqual(len(projectsGetEntries()), 1)
        self.assertEqual(len(projectsCategoriesGetEntries()), 1)

        # assert that the category is associated with the id
        self.assertEqual(len(projectsGetEntries()[0].get("categories")), 1)
    
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
        r = sendRequest("GET", self.URL)
        self.assertEqual(len(r.json()), 1)
    
    def testDelete(self):
        """Test case for /projects/:id/categories/:id"""
        r = sendRequest("DELETE", f"{self.URL}/{self.category_id}")
        self.assertEqual(len(projectsCategoriesGetEntries()), 0)
    
    def testPost(self):
        r = sendRequest("POST", self.URL, data=TEST_DATA_PROJECT_CATEGORY)
        # check that there are 2 categories
        self.assertEqual(len(projectsCategoriesGetEntries()), 2)
        # check that there is a new category associated with the id
        self.assertEqual(len(projectsGetEntries()[0].get("categories")), 2)

if __name__ == "__main__":
    unittest.main()