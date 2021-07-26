# **TODO app**
This guide specifies how to setup this project for development environment.

### Prerequisite: install and setup postgresql
  - go to "https://brew.sh/", download the lastest version of homebrew;
  - execute `brew install postgresql` in CMD, or install from https://www.postgresql.org/download/
  - execute `CREATE DATABASE todo_db;` to create database.
  - execute `create role postgres superuser;`
  - if you donot have python3, install by executing `brew install python3` or install from https://www.python.org/downloads/"

## Create VENV and install requirements
   open terminal and execute command:
  > - `python3 -m venv <path_to_env>`
  > - `source <path_to_env>/bin/activate`
  > - `pip install -r <path_to_app_folder>/requirements.text`

## Run the project
   In terminal, with activated venv, execute:
  > `uvicorn app:app --reload`


## Api Endpoints:
1 - **get todo item by id:**
> GET url -> base_url/item/{item_id}

2 - **create todo item:**
> POST url -> base_url/item
```
request body
{
  "id": 1,
  "title": "string",
  "description": "string"
}
```
3 - **update todo item:**
> PUT url -> base_url/item/{item_id}
```
request body
{
  "title": "string",
  "description": "string"
}
```
4 - **delete todo item:**
> DELETE url -> base_url/item/{item_id}

5 - **get todo item list:**
> GET url -> base_url/item/all
