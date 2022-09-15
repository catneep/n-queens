FROM python:3

WORKDIR /Client

COPY requirements.txt ./
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD [ "python", "./main.py" ]

EXPOSE 443