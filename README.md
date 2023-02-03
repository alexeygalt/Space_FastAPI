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
  
  Clicking the `authorize` button will bring up a screen like this:
  ![Third][screenshot_3]
  Now you can check all API's


## Further modifications


* This template uses OAuth2 based authentication and it's easy to change that. FastAPI
docs has a comprehensive list of the available [authentication][fastapi_security]
options and instructions on how to use them.

* You can change the application settings  in the `.env` file.(check .env.example)

## Stack


* [Docker][docker]
* [FastAPI][fastapi]
* [Pydantic](https://pydantic-docs.helpmanual.io/)
* [Pytest](https://docs.pytest.org/en/latest/)
* [Uvicorn][uvicorn]
  


[fastapi]: https://fastapi.tiangolo.com/
[fastapi_security]: https://fastapi.tiangolo.com/tutorial/security/
[docker]: https://www.docker.com/
[uvicorn]: https://uvicorn.org/
[screenshot_1]: https://user-images.githubusercontent.com/108652145/216345396-1e2a78b8-27a4-4f34-b7c1-9a7256f447dd.png
[screenshot_2]: https://user-images.githubusercontent.com/108652145/216350326-e4e4b87d-d523-4ac5-913f-2b5c51268735.png
[screenshot_3]: https://user-images.githubusercontent.com/108652145/216535222-8b0f56a8-6d17-49a2-a998-51a953a275b1.png