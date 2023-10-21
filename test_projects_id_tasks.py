import unittest

from helper_functions import *


class TestProjectsIdTasks(unittest.TestCase):
    def setUp(self):
        ## wipe all id and categories data
        self.assertTrue(projectsSetUp("projects"))
        ## add entry and get id
        r = sendRequest("POST", "projects", data=TEST_DATA_PROJECT)
        self.id = r.json().get("id")
        self.URL = f"projects/{self.id}/tasks"
        ## add category and get id
        r = sendRequest("POST", self.URL, data=TEST_DATA_PROJECT_TASKS)
        self.task_id = projectsTasksGetEntries()[0].get("id")

        # assert that there is one id and one category
        self.assertEqual(len(projectsGetEntries()), 1)
        self.assertEqual(len(projectsTasksGetEntries()), 1)
    
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
        """Test case for /projects/:id/categories/:id"""
        r = sendRequest("DELETE", f"{self.URL}/{self.task_id}")
        self.assertEqual(len(projectsTasksGetEntries()), 0)

    def testGet(self):
        r = sendRequest("GET", self.URL)
        self.assertEqual(len(r.json()), 1)
    
    def testPost(self):
        r = sendRequest("POST", self.URL, data=TEST_DATA_PROJECT_TASKS)
        # check that there are 2 categories
        self.assertEqual(len(projectsTasksGetEntries()), 2)
        # check that there is a new category associated with the id
        self.assertEqual(len(projectsGetEntries()[0].get("tasks")), 2)
    
    def testPostWithID(self):
        """Undocumented case like test_todos_id_taskof.py"""
        # create new id
        r = sendRequest("POST", "projects", data=TEST_DATA_PROJECT)
        id = r.json().get("id")
        # associate existing taskof with new id
        url = f"projects/{id}/tasks"
        r = sendRequest("POST", url, data={"id": self.task_id})
        # check that the both id are associated with the existing taskof
        id1_task = projectsGetEntries()[0].get("tasks")
        id2_task = projectsGetEntries()[1].get("tasks")
        self.assertEqual(len(id1_task), 1)
        self.assertEqual(len(id2_task), 1)
        # check that both id have same taskof id
        self.assertEqual(id1_task[0].get("id"), id2_task[0].get("id"))

if __name__ == "__main__":
    unittest.main()
    print(projectsTasksGetEntries())
    print(projectsTasksGetEntries()[0].get("id"))