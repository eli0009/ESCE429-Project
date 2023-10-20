# Project members
- Enlai Li 261068637
- Shyam Desai 260947829

## Roles
- Exploratory testing: Both
- Unit Testing (code, video): Enlai Li
- Report (summaries, bugs): Shyam Desai

# Capabilities

## /todos/:id/tasksof
- Create new task if no task id is specified
- Add a task to specified :id
- Add existing task to id by specifying task id in body
```json
{
    "id": "4",
    "title": "Test Taskof Title",
    "completed": false,
    "active": false,
    "description": "Test Taskof description"
}
```
  


# GUIDE

## Running all tests at once
To run tests, run the following command inside current directory. The packages unittest and requests are required. This will run test from every test module
> Linux
```bash
bash run_unittests.sh
```
> Other
```bash
python3 -m unittest discover -p "test_*.py"
```

## Running one module at a time
Replace everything under, and including `if __name__ == "__main__":` with:
```python
if __name__ == "__main__":
    unittest.main()
```
Afterward, simply run the python file
# Notes

- The unittest framework already runs the tests in random order so there is no need to worry about determining order using pseudo random number generation
