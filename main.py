import unittest


class TestYourFunctions(unittest.TestCase):

    def setUp(self):
        # Set up resources needed for tests
        self.data = [1, 2, 3, 4]

    def tearDown(self):
        # Clean up resources after tests
        self.data = None