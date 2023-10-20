import unittest

from helper_functions import *


class TestTodosIdTaskof(unittest.TestCase):
    def setUp(self):
        # wipe database
        self.assertTrue(todosSetUp("todos"))
