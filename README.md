# OpenFoodFacts - Openclassrooms project 5

The idea of Pur Beurre is to create a program that interacts with the OpenFoodFacts database. This program makes it possible to recover food from the database of OpenFoodFacts, compare them and offer the user a healthier substitute to the food that he chose previously. : [link to github](https://github.com/Romderful/Project5_Openfoodfacts)

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
