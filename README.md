# Hangman

Simple hangman app

# Get started

## install dependencies

Before you can run the app, make sure to run this command:

```
pip install -r requirements.txt
```

If you have multiple versions of python installed, you may need to use `pip3` instead

```
pip3 install -r requirements.txt
```

## running the app

To start the game:

```
python main.py
```

## running the test

To run all the tests:

```
python -m unittest
```

To run the subset of tests in the directory e.g. `hangman`

```
python -m unittest discover -s hangman
```

To run the specific test file

```
python -m unittest <path_to_file>

e.g.
python -m unittest hangman/test/test_startup.py
```
