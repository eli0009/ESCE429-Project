import unittest

from helper_functions import *

if __name__ == "__main__":
    sendRequest("GET", "http://localhost:4567/projects", True)
    sendRequest("HEAD", "http://localhost:4567/projects", True)