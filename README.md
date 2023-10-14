# FORNOVA Interview Exercise

App consisting of two parts (FastAPI for backend and Flask for frontend).

## Running the app

### Dockerized approach
1. cd into root directory (where **docker-compose.yaml** is located)
2. `docker compose up --build`
3. visit _`http://localhost:3000/hotels`_


### Bare metal approach
1. cd into **backend**
2. `. env/bin/activate`
3. `pip install -r requirements.txt` **Only if you are running it first time for this virtual env**
4. `uvicorn main:app`
5. Open another teminal and `cd` into **frontend**
6. `. env/bin/activate`
7.  `pip install -r requirements.txt` **Only if you are running it first time for this virtual env**
8. open `.env` file and edit **BACKEND_HOST** value to `localhost:8000`
9. `flask run`
10. visit _`http://localhost:5000/hotels`_

### Showcase:
![Hotels Browser showcase](https://github.com/MarjanStojanov/fornova_interview/assets/38865278/38b5d75f-32dd-4217-893f-7ba8b9c1e6b2)
