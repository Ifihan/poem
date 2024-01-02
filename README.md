# Poem Generator

A poem generator that generates poems using the [MakerSuite](https://makersuite.google.com/app/home) API.

https://github.com/Ifihan/poem/assets/49107589/2332ec16-92bc-4e08-bd95-fb74e0803ad4

## Getting Started

To run this project locally, you need to follow the following steps:

1. Install [Python](https://www.python.org/downloads/) (if you don't have it installed).

2. Clone the repository.

```bash
git clone https://github.com/Ifihan/poem.git
```

3. Set up and activate a virtual environment (virtualenv)

```bash
pip install virtualenv
python -m venv env
source env/bin/activate
```

4. Install the dependencies

```bash
pip install -r requirements.txt
```

5. Duplicate the `env.example` file and rename it to `.env` and fill in the required details.

6. Grab your API keys from [MakerSuite](https://makersuite.google.com/app/apikey) and fill in the required details in the `.env` file.

7. Run the application

```bash
set FLASK_APP=app.py # Windows
export FLASK_APP=app.py # Linux/ Mac
flask run
```

8. You're good to go!

## To do

- Ensure that it's only poems it'll generate.
- Grab the poem "idea" and make it the topic (30% done).

## Any issues?

Kindly submit an [issue](https://github.com/Ifihan/poem/issues), thank you!

## License?

Will be updated soon.

While you're here, give a star ⭐ to the repo if you like this project.
