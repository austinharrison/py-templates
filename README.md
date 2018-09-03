# py\_template

This is a very basic starting point for a python project that can be deployed in a docker container. 
Basic logging is setup, as well as basic credential management using a YAML file.

## Environments
### Installing and activating
Python was installed using Anaconda but we want to use `pip` instead of `conda`. To start with a clean slate, create a new conda environment then create the virtualenv which will be copied to the ./venv/ folder.
```
conda create -n blank37 python=3.7
activate blank37
python -m venv venv
deactivate
```
for windows
```
venv\Scripts\activate.bat 
```
for linux
```
source venv/bin/activate
```
### Installing packages and creating requirements.txt
With the environment active:
```
pip install pyyaml
pip freeze > requirements.txt
```

### Installing packages from requirements.txt
To install packages in the requirements.txt file, with the new environment activated:
```
pip install -r requirements.txt
```

## Credentials
The credentials aren't saved in the git repo for security reasons. Credentials will be saved in `creds/creds.yml`.
An example `creds.yml` file will be created if one doesn't exist and should be modified with real credentials.

### creds/creds.yml example
```
example:
  username: username
  password: password
```

## Running as a docker container
The script in `main.py` can easily be run in a docker container by running the command
`docker-compose up`. The docker image will be built using python 3.7 as a base image and will
install all packages in `requirements.txt`.

The docker container will execute `init.sh` which simply runs `python main.py`. This can be modified
to run any other python script or other bash commands in the container.

The current directory will be mounted in the container so all logs and other files will be 
saved on the host machine.

## TODO
+ Put setup process somewhere else besides `main.py`
+ Have `logging` get config from a file
