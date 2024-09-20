# Project Management CLI

A Command-Line Interface (CLI) application for managing users, projects, and tasks. This CLI tool allows you to perform CRUD (Create, Read, Update, Delete) operations on users, projects, and tasks efficiently.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Technologies Used](#technologies-used)
- [Contributions](#contributions)

## Installation
```
# clone the repo
$ git clone <repo link>
```
```
# navigate to directory
$ cd <directory name>
```
```
# install dependencies and create virtual environment
$ pipenv install & pipenv shell
```
```
# run the application
$ python main.py
```

 ## Usage
 ```
 # list available commands
 $ python main.py --help
 ```   
 ```
 # to get help for specific command, for example user-related commands;
 $ python main.py user --help
 ```

## Commands
```User management```
```
# create new user
$ python main.py user create
```
```
# list users
$ python main.py user list
```
```
# update user
$ python main.py user update
```
```
# delete user
$ python main.py user delete 
```
```Project management```   
```
# create new project
$ python main.py project create
```
```
# list projects
$ python main.py project list
```
```
# update project
$ python main.py project update
```
```
# delete project
$ python main.py project delete 
``` 
```Task management```   
```
# create new task
$ python main.py task create
```
```
# list tasks
$ python main.py task list
```
```
# update task
$ python main.py task update
```
```
# delete task
$ python main.py task delete 
``` 

# Technologies used
- Python
- SQL Alchemy
- Click

# Contributions
Authored by Shalyne Chepngeno


