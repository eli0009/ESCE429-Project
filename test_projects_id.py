import unittest

from helper_functions import *


class TestProjectsId(unittest.TestCase):
    def setUp(self):
        self.assertTrue(projectsSetUp("projects"))
        # add entry and get id
        r = sendRequest("POST", "projects", data=TEST_DATA_PROJECT)
        self.id = r.json().get("id")
        self.URL = f"projects/{self.id}"
    
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
        self.assertEqual(projectsGetEntries()[0].get("id"), self.id)
    
    def testPut(self):
        """Amend the entry"""
        new_data = {**TEST_DATA_PROJECT}
        new_data["title"] = "new title"
        sendRequest("PUT", self.URL, data=new_data)
        self.assertEqual(projectsGetEntries()[0].get("id"), self.id)
        self.assertEqual(projectsGetEntries()[0].get("title"), "new title")
    
    def testPost(self):
        """same as put"""
        new_data = {**TEST_DATA_PROJECT}
        new_data["title"] = "new title"
        sendRequest("POST", self.URL, data=new_data)
        self.assertEqual(projectsGetEntries()[0].get("id"), self.id)
        self.assertEqual(projectsGetEntries()[0].get("title"), "new title")
    
    def testPostNewID(self):
        """Check that this method confroms to the API by not allowing a new id to be specified"""
        new_id = int(self.id) + 1
        r = sendRequest("POST", f"projects/{new_id}", data=TEST_DATA_PROJECT)
        self.assertIsNone(r)
    
    def testDelete(self):
        r = sendRequest("DELETE", self.URL)
        self.assertEqual(len(projectsGetEntries()), 0)

if __name__ == "__main__":
    unittest.main()
