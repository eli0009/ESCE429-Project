import unittest

from helper_functions import *


class TestProjects(unittest.TestCase):
    
    def setUp(self):
        self.URL = "projects"
        self.assertTrue(projectsSetUp("projects"))
    
    def testXML(self):
        r = sendRequest("GET", self.URL, payload_type="xml")
        self.assertTrue(isXML(r))
    
    def testJSON(self):
        r = sendRequest("GET", self.URL, payload_type="json")
        self.assertTrue(isJSON(r))
    
    def testHead(self):
        r = sendRequest("HEAD", self.URL)
        self.assertTrue(isHEAD(r))
    
    def testAddEntry(self):
        r = sendRequest("POST", self.URL, data=TEST_DATA_PROJECT)
        # check data was added
        self.assertEqual(len(projectsGetEntries()), 1)
    
    def testGet(self):
        """add 5 entries and get them all"""
        for i in range(5):
            sendRequest("POST", self.URL, data=TEST_DATA_PROJECT)
        self.assertEqual(len(projectsGetEntries()), 5)
    


if __name__ == "__main__":
    print(projectsGetEntries())
    # todosSetUp("todos")
    print(projectsSetUp("projects"))
    print(projectsGetEntries())