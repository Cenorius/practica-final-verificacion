Master Status: [![Build Status Master](https://travis-ci.org/Cenorius/practica-final-verificacion.svg?branch=master)](https://travis-ci.org/DarkAnHell/practica-final-verificacion)

Dev Status: [![Build Status Dev](https://travis-ci.org/Cenorius/practica-final-verificacion.svg?branch=dev)](https://travis-ci.org/DarkAnHell/practica-final-verificacion)

To be able to execute this project you need to install some packages. Follow this instructions:

- Create a new virtual environment `virtualenv ENV`
- Load it `source ENV/bin/activate`
- Now install the packages with `pip install -r requirements.txt` (if you don't have `pip` installed you'll have to do it)
- Now, if you want to just run the project, execute `python2.7 main.py` and open `http://localhost:5000` to access to the web interface
- If you also want to run the BDD and Selenium tests, do the following `cd tests && lettuce` while `main.py` is also running
- If you just want to run all the other tests, execute `make test`

### WARNING
We know that there is a `SECRET_KEY` disclosure in the `config.py` file and `DEBUG` is enabled. This project is an academic example. Please don't use this code in any production environment.
