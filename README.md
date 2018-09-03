# py\_template

This is a very basic starting point for a python project that can be deployed in a docker container. 

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

### creds/creds.yml example
```
example:
  username: username
  password: password
```
