# Simple space api 1.0

## Description

This is a minimalistic[FastAPI][fastapi] application.
It's suitable for developing small to medium sized API oriented micro-services.

## Features

* It uses [FastAPI][fastapi] framework for API development. FastAPI is a modern, highly
performant, web framework for building APIs with Python 3.6+.

* OAuth2 (with hashed password and Bearer with JWT) based authentication

* Dockerized using **python:3.11-slim** and optimized for size and
functionality.

## Quickstart

### Run the app in containers

- Clone the repo and navigate to the root folder.
```shell
docker-compose up
```

### Or, run the app locally
- Install requirements
```shell
pip install -r requirements.txt
```
- Run tests
```shell
pytest .
```
```shell
pytest . --cov
```
- Run project
```shell
 uvicorn space_app.app:app --reload   
```

### Check the APIs

* To play around with the APIs, go to the following link on your browser:

    ```
    http://127.0.0.1:8000/docs/
    ```
  This will take you to an UI like below:
  ![First][screenshot_1]
  Send POST to auth/sing-up and create new user.

 
* Press the authorize button on the right and add username and password. The APIs use OAuth2 (with hashed password and Bearer with JWT) based authentication. In this case, the username and password is ubuntu and debian respectively.
  ![Second][screenshot_2]



[fastapi]: https://fastapi.tiangolo.com/

[screenshot_1]: https://user-images.githubusercontent.com/108652145/216345396-1e2a78b8-27a4-4f34-b7c1-9a7256f447dd.png
[screenshot_2]: https://user-images.githubusercontent.com/108652145/216350326-e4e4b87d-d523-4ac5-913f-2b5c51268735.png