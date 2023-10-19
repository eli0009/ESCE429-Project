import json
import unittest

from helper_functions import *


class TestTodo(unittest.TestCase):
    def test(self):
        self.assertEqual(True, True)


if __name__ == "__main__":
    unittest.main()
    # r = requests.post("http://httpbin.org/post", json={"test": "cheers"})
    # print(r.status_code)

    # sendRequest("GET", "http://localhost:4567/todos", True)
    # sendRequest("HEAD", "http://localhost:4567/todos", True)

    data = {
        "title": "officia deserunt mol",
        "doneStatus": True,
    }
    r = sendRequest(
        "POST",
        "todos",
        True,
        data,
        payload_type="xml",
    )
    # print(r.json().get("id"))
