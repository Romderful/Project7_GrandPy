# GrandPy Bot - Openclassrooms project 7

This project is a web application that allows you to chat with a robot. This robot attempts to return the address or location given in the user message, as well as an anecdote of the surroundings.

## Installation

Clone [the repository](https://github.com/Romderful/Project7_GrandPy) on your computer.


Set your virtual environment under [python 3.9](https://www.python.org/downloads/release/python-392/)


```bash
python -m venv .venv  # create the virtual environment
. .venv/Scripts/activate  # activate the virtual environment
pip install -r requirements.txt  # install the dependencies

touch .env # create a file where you'll put your mysql server informations

HERE_REST_API_KEY="your_api_key"
HERE_JS_API_KEY="your_api_key"
```

## Usage

```bash
python main.py
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
