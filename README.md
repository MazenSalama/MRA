### README


### Running the locally
#### Method 1
+ Setup a virtual env using pipenv
```bash
pip install pipenv
pipenv install 
```

+ Running the app
```bash
export FLASK_ENV=development
flask run 
```


#### Method 2
+ If you already have flask and Flask-SQLAlchemy installed
```bash
export FLASK_ENV=development
flask run 
```

or 
```bash
python3 app.py 
```

#### Initializing the Database
+ Incase you want to test it locally you can try this approach
+ You will have to open python from the same location the `app.py` file is from your terminal.

```python
>>>from app import db 
>>>db.create_all()
```
+ Then you can exit from your python REPL
+ You can now input your data into the form


#### Using MYSQL
+ There is a place for the SQLALCHEMY_DATABASE_URI  where you can replace the link to your mysql dataset
+ I used sqlite3 which is compatible with all operating systems
```python
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"  
# Change this place to mysql url ========
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://scott:tiger@localhost/mydatabase"

```


#### App Structure
```
.
├── app.py
├── images
│   ├── app_images01.png
│   ├── app_images02.png
│   └── app_images03.png
├── Pipfile
├── Pipfile.lock
├── __pycache__
│   └── app.cpython-36.pyc
├── resource.txt
├── static
│   ├── css
│   │   ├── bootstrap.css
│   │   ├── font-awesome.min.css
│   │   └── style.css
│   ├── fonts
│   │   ├── FontAwesome.otf
│   │   ├── fontawesome-webfont.eot
│   │   ├── fontawesome-webfont.svg
│   │   ├── fontawesome-webfont.ttf
│   │   ├── fontawesome-webfont.woff
│   │   └── fontawesome-webfont.woff2
│   ├── img
│   │   └── avatar.png
│   └── js
│       ├── bootstrap.min.js
│       ├── jquery.min.js
│       └── tether.min.js
├── templates
│   ├── base.html
│   ├── details.html
│   ├── index.html
│   └── search.html
└── users.db


```

#### Thank you very much
+ Let me know the outcome. Thanks once again