# FROM postgres
FROM python:3

WORKDIR /App

COPY requirements.txt ./
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD [ "python", "./main.py" ]