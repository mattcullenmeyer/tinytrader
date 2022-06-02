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
`$ touch .env.db`

Populate the .env and .env.db files based on the .env.template and .env.db.template, respectively

### Install Dependencies

Install frontend packages with npm:  
`$ npm install`

Create a virtual environment, activate and install dependencies:

```
$ sudo pip3 install virtualenv
$ virtualenv venv --python=python3
$ source venv/bin/activate
$ pip3 install -r requirements.txt
$ python manage.py migrate
```

### Docker

`$ make docker-dev-all`  
Visit http://localhost:8000/

### Run Server

With the virtual environment still active, run the following command to run the server:  
`$ python manage.py runserver`

Navigate to `http://127.0.0.1:8000/` to see the site.

Create a super user to log into admin:  
`$ python manage.py createsuper`

### Create Staging Environment

- Deploy server using Terraform and Ansible with https://github.com/mattcullenmeyer/terraform-tinytrader
- Update DNS record to staging IP address
- SSH into the newly provisioned DigitalOcean Droplet as user matt
- `$ git clone https://github.com/mattcullenmeyer/tinytrader.git`
- `$ nano .env`
  - Populate with required environment variables
  - ALLOWED_HOSTS should be IP Address of droplet and staging.tinytrader.io
- `$ nano .env.db` and populate
- Install make, docker compose and certbot (this should eventually transition to Ansible playbook)
  - `$ sudo apt-get update`
  - `$ sudo apt-get install make`
  - `$ sudo apt-get install docker-compose-plugin`
  - `$ sudo apt-get install certbot`
- Start up docker-compose.dev.yml to ensure everything is set up correctly
  - `$ docker compose -f docker-compose.dev.yml up -d --build`
  - Check the IP address of the droplet at port 1337 in your browser to ensure website is up
- Take down docker-compose.dev.yml, including volumes
  - `$ docker compose -f docker-compose.dev.yml down -v`
- Ensure the updated DNS A record has progated
  - `$ dig staging.tinytrader.io`
  - A record should be the IP adddress of the newly provisioned droplet
- Create a fake SSL certificate so nginx can start up without errors
  - `$ sudo certbot certonly --standalone --preferred-challenges http -d staging.tinytrader.io`
- Start up docker-compose.staging.yml and then request SSL certificate
  - `$ docker compose -f docker-compose.staging.yml up -d --build`
  - `$ docker compose -f docker-compose.staging.yml run --rm certbot certonly --webroot -w /var/lib/letsencrypt/ -d staging.tinytrader.io`
- Navigate to staging.tinytrader.io in the browser, which should be up and secure
