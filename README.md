# Basic Python Flask Web App
## Project Setup (Terminal - MacOS)

```
$ mkdir proj_name
$ cd proj_name
$ python3 -m venv myenv
$ source myenv/bin/activate
(myenv) $ python3 -m pip install Flask
```

## Run Flask Development Server

1. Create basic **app .py** file at route of project
```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
```

2. Run **app .py** via terminal
`(myenv) $ python3 app.py`

## Transform Project into a Package

1. Create package folder
`(myenv) $ mkdir my_pkg`

2. Move **app .py** into new folder
3. Rename **app .py** to **__init __ .py**
`(myenv) $ mv app.py my_pkg/__init__.py`

4. Run Flask Project (Terminal - MacOS)
`(myenv) $ python3 -m flask --app my_pkg >=run --port 8000 --debug`

## Incorporate Application Factory + Blueprints

1. Instead of having application’s code at the root level of the **__init __ .py** file, work with a function that returns your application.
```
from flask import Flask

def create_app():
	app = Flask(__name__)
	return app*=
```

2. Create modules that contain related views that are conveniently imported in **__init __ .py**.

> a. Create **page .py** file in *my_pkg*
> ```
> from flask import Blueprint
> 
> bp = Blueprint("pages", __name__)
> 
> @bp.route("/")
> def home():
> 	return "Hello, Home Page!"
> 
> @bp.route("/about")
> def about():
> 	return "Hello, About Page!"
> ```
> 
> b. Import **page .py** Blueprints into **__init __ .py**
> ```
> from flask import Flask
> from board import pages
> 
> def create_app():
> 	app = Flask(__name__)
> 	app.register_blueprint(pages.bp)
> 	return app
> ```

3. Navigate to http://127.0.0.1:8000/ and http://127.0.0.1:8000/about in browser to validate changes.

## Resources
[Demo via RealPython.com](https://realpython.com/flask-project/)<!-- {"preview":"true"} -->