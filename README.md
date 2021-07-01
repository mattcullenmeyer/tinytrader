## TinyTrader

TinyTrader is a web app for quantitative stock analysis developed using Django and React.

### Getting Started

Get started by cloning the repo:   
`$ git clone https://github.com/mattcullenmeyer/tinytrader.git`

Once cloned, navigate to the root directory of the project:   
`$ cd tinytrader`

### Install Postgresql

Download Postgresql and create a database called `tinytrader`. Create a new user with all privileges. Keep track of username and password for environmental variables in next step.

### Add Environmental Variables

Create a file to store environmental variables:   
`$ touch .env`   

Add the following environmental variables and associated values to the .env file, which is ignored in version control:
```
SECRET_KEY=<secret key>
DEBUG=True
DATABASE_NAME=tinytrader
DATABASE_USERNAME=<database username>
DATABASE_PASSWORD=<database password>
```

### Install Dependencies

Install frontend packages with npm:  
`$ npm install`  

Create a virtual environment, activate and install dependencies:
```
$ pip3 install virtualenv
$ virtualenv env --python=python3
$ source env/bin/activate
$ pip3 install -r requirements.txt
$ python manage.py migrate
```

### Run Server

With the virtual environment still active, run the following command to run the server:   
`$ python manage.py runserver`

Navigate to `http://127.0.0.1:8000/` to see the site.

Create a super user to log into admin:   
`$ python manage.py createsuper`
