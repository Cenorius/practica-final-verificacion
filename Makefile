init:
	pip install -r requirements.txt

test:
	nosetests tests

coverage:
	coverage run textprocessor/core.py
	coverage report -m

clean:
	find . -type f -name '*.pyc' -delete