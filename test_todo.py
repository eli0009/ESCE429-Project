import json
import unittest

from helper_functions import *

if __name__ == "__main__":
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
    )
    print(r.json().get("id"))

    # sendRequest("POST", "http://localhost:4567/todos", True, data)
