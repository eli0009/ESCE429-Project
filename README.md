# Project members
- Enlai Li 261068637
- Shyam Desai 260947829

## Roles
- Exploratory testing: Both
- Unit Testing (code, video): Enlai Li
- Report (summaries, bugs): Shyam Desai

# Description

This folder contains one file for each API endpoint (module), and each file contains at least one unit case for each method described in the documentation, for a total of 50 unit tests.

## Notes

- The unittest framework already runs the tests in random order so there is no need to worry about determining order using pseudo random number generation
- The database is wiped and filled with test value before each of the 50 unit tests in order to ensure that they can be run in any order, making each test truly independent


# Capabilities

## /todos/:id

### DELETE
- Deleting an id also deletes all taskof and categories associated with it

## /todos/:id/tasksof

### POST
- Create new task if no task id is specified (undocumented behavior)
- Add a task to specified :id
- Add existing task to id by specifying task id in body
- Example request for `http://localhost:4567/todos/1/tasksof`
```json
# POST body
{
    "id": "4",
    "title": "Test Taskof Title",
    "completed": false,
    "active": false,
    "description": "Test Taskof description"
}

# undocumented behavior body
{
    "title": "Test Taskof Title",
    "completed": false,
    "active": false,
    "description": "Test Taskof description"
}
```

## /projects
- Projects seem to be linked with `/todos/:id/tasksof`. Any task created will appear in projects, however deleting ids with not delete any project
- Deleting a project will delete its categories and taskof, just like todos


## /projects/:id
## POST
- Works the same way as PUT

# Bugs

## /todos/:id/categories
### GET
- Returns every single category even if an :id is specified, ex
`http://localhost:4567/todos/1/categories` will return all categories even if `id = 1` was specified. This is unexpected because it was specified in the documentation that only categories for specific id will be returned
```json
# ID response
{
    "todos": [
        {
            "id": "20",
            "title": "officia deserunt mol",
            "doneStatus": "true",
            "description": "deserunt mollit anim",
            "categories": [
                {
                    "id": "8"
                }
            ]
        }
    ]
}

# Category response
{
    "categories": [
        {
            "id": "8",
            "title": "Whatever",
            "description": "This is a description"
        }
    ]
}
```

## /todos/:id/tasksof
### POST
- This bug is detailed in the file `test_todos_id_taskof.py` in the function `BUGGEDtestPostWithID()`, basically when you create a new taskof with an existing taskof ID, you will find that there are 2 taskof entries with same ID, which makes no sense because ID are supposed to be unique

## /projects/:id/tasks
### GET
- Same problem as it's /todos counterpart, specifying id is useless because it will always return everything

# Howto

## Running all tests at once
To run tests, run the following command inside current directory. The python packages unittest and requests are required. This will run test from every test module
> Linux
```bash
bash run_unittests.sh
```
> Other
```bash
python -m unittest discover -p "test_*.py"
```

## Running one module at a time
> using command-line

Run the following in terminal, replace "filename.py" with the name of the python test file
```bash
python -m unittest discover -p "filename.py"
# example
python -m unittest discover -p test_todos.py
```
> running files

Replace everything under, and including `if __name__ == "__main__":` with:
```python
if __name__ == "__main__":
    unittest.main()
```
Afterward, simply run the python file
