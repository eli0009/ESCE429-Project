import unittest

from helper_functions import *


class TestTodosIdTaskof(unittest.TestCase):
    def setUp(self):
        # wipe database
        self.assertTrue(todosSetUp("todos"))
        # add entry and get id
        self.r = sendRequest("POST", "todos", data=TEST_DATA_ID)
        self.id = self.r.json().get("id")
        self.URL = f"todos/{self.id}/tasksof"
        # add category and get id
        r = sendRequest("POST", self.URL, data=TEST_DATA_TASKOF)
        self.taskof_id = todosTaskofGetEntries()[0].get("id")

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
        """Test case for /todos/:id/tasksof/:id"""
        r = sendRequest("DELETE", f"{self.URL}/{self.taskof_id}")
        self.assertEqual(len(todosTaskofGetEntries()), 0)

    def testGet(self):
        r = sendRequest("GET", self.URL)
        self.assertEqual(len(r.json().get("projects")), 1)

    def testPostNoID(self):
        """Test case for documented behaviour, no id"""
        r = sendRequest("POST", self.URL, data=TEST_DATA_TASKOF)
        # check that there are 2 taskof
        self.assertEqual(len(todosTaskofGetEntries()), 2)
        # check that there are 2 taskof associated with the id
        self.assertEqual(len(todosGetEntries()[0].get("tasksof")), 2)

    def testPostWithID(self):
        """Undocumented case where you specify an id in POST body, which will allow
        you to associate an existing taskof with an id"""
        # create new id
        r = sendRequest("POST", "todos", data=TEST_DATA_ID)
        id = r.json().get("id")
        # associate existing taskof with new id
        url = f"todos/{id}/tasksof"
        r = sendRequest("POST", url, data={"id": self.taskof_id})
        # check that the both id are associated with the existing taskof
        id1_task = todosGetEntries()[0].get("tasksof")
        id2_task = todosGetEntries()[1].get("tasksof")
        self.assertEqual(len(id1_task), 1)
        self.assertEqual(len(id2_task), 1)
        # check that both id have same taskof id
        self.assertEqual(id1_task[0].get("id"), id2_task[0].get("id"))

    def BUGGEDtestPostWithID(self):
        """BUG for undocumented case where you specify an id in POST body"""
        # create new id
        r = sendRequest("POST", "todos", data=TEST_DATA_ID)
        id = r.json().get("id")
        # associate existing taskof with new id
        url = f"todos/{id}/tasksof"
        r = sendRequest("POST", url, data={"id": self.taskof_id})
        # check that no new taskof was created
        """
        The bug occurs here, where there is more than one taskof in the database, even though both taskof have the same ID.
        You can verify through the assertion below that it has more than one taskof, even though it should only have one.
        """
        self.assertNotEqual(len(todosTaskofGetEntries()), 1)
        """
        Check that both taskof entries have same ID, which confirms the bug
        """
        # pprint(todosTaskofGetEntries())
        task1 = todosTaskofGetEntries()[0]
        task2 = todosTaskofGetEntries()[1]
        self.assertEqual(task1.get("id"), task2.get("id"))


if __name__ == "__main__":
    # unittest.main()
    todosSetUp("todos")
