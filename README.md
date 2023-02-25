# Ryde Technical Exercise

A RESTful API that can get/create/update/delete user data from a persistence database.

## Requirements

| Requirements | Version |
| ------------ | ------- |
| Python       | 3.10.0  |
| FastAPI      | 0.92.0  |
| MongoDB      | 6.0     |

## Running locally

1. If you don't have MongoDB installed on your machine, refer to the [Installation](<(https://www.mongodb.com/docs/manual/installation/)>) guide from the docs. Once installed, continue with the guide to run the [mongod](https://www.mongodb.com/docs/manual/reference/program/mongod/#bin.mongod) daemon process.

2. Activate your python virtual env and install dependencies
   ```
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Update `DATABASE_URL` in `.env` with your MongoDB url.
4. Then you can run the app with
   ```
   python server.py
   ```

App can be accessible at

```
http://127.0.0.1:8000/
```

Check API is working by running

```
http://127.0.0.1:8000/api/ping
```

### Documentation

Documentation for API can be found at

```
http://127.0.0.1:8000/docs
```
