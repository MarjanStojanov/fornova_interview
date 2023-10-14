FROM python:3.11-slim

WORKDIR /opt

COPY . .

RUN pip install -r requirements.txt

CMD [ "flask", "run", "--host=0.0.0.0", "--port=4000"]
