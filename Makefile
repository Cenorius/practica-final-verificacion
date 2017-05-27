init:
	pip install -r requirements.txt

test:
	nosetests tests

coverage:
	coverage run textprocessor/core.py
	coverage report -m

clean:
	rm -rf */*.pyc