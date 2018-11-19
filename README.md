# Installation

## After cloning
```
[sudo] pip install virtualenv
virtualenv venv
``` 

## Activate Environment

```
# Linux/UNIX or Windows git-bash-cli
source venv/bin/activate # or . venv/bin/activate

# Windows cmd
venv/Scripts/activate

# Windows powershell solution 1
Set-ExecutionPolicy AllSigned 
./venv/Scripts/activate # Answer yes to trust the signer

# Windows powershell solution 2 (if solution 1 fails)
Set-ExecutionPolicy RemoteSigned
./venv/Scripts/activate # Answer yes to trust the signer
```

## Install Requirements
```
pip install -r requirements.txt
```

## Run the project WITHOUT heroku-cli

Windows users should use `set` instead of `export`, example: `set FLASK_APP=app.py`

```
export FLASK_APP=app.py
export FLASK_DEBUG=1 #Enables reload :)
flask run
```

## Running the project WITH heroku-cli
Remember you should have installed `heroku-cli` to simulate a heroku server. To
have the full experience of a heroku instance on your local machine it is recommended
to use a linux/UNIX machine with `gunicorn`.
Create a `.env` file and add your environment variables as you need

```
FLASK_APP=app.py
FLASK_DEBUG=1
```

- `heroku local` for unix/linux users
- `heroku local -f Procfile.windows` for windows users

