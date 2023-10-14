import unittest

from helper_functions import *

if __name__ == "__main__":
    sendRequest("GET", "http://localhost:4567/todos", True)
    sendRequest("HEAD", "http://localhost:4567/todos", True)

    data = """'title': "create paperwork"""
    sendRequest(
        "POST",
        "http://localhost:4567/todos",
        True,
        data,
    )

    # sendRequest("POST", "http://localhost:4567/todos", True, data)
