install:
    pip install --upgrade pip &&\
    pip install -r requirements.txt

test:
    python -m pytest -vv test_flask_api.py


lint:
    pylint --disable=R,C api.py

all: install lint test