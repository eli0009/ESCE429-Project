import unittest
from helper_functions import *
import json

url = 'http://localhost:4567/todos'

headers = {
    'Content-type':'application/json', 
    'Accept':'application/json'
}

if __name__ == "__main__":
   sendRequest("GET", url, True)
   sendRequest("HEAD", url, True)

data = json.dumps({
  "title": "testing paperwork",
  "doneStatus": False,
  "description": ""
})
sendRequest("POST", url, True, data)