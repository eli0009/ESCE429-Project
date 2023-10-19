# GUIDE

To run tests, run the following command inside current directory. The packages unittest and requests are required
## Linux
```
bash run_unittests.sh
```
## Other
```
python3 -m unittest discover -p "test_*.py"
```

# Notes

- The unittest framework already runs the tests in random order so there is no need to worry about determining order using pseudo random number generation
