# Simple space api 1.0

## General Information
Simple API to space Stations
- You can check project at with swagger : `http://127.0.0.1:8000/docs/`

## Install:

- Run with Docker:
```shell
docker-compose up
```

- Local:
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

