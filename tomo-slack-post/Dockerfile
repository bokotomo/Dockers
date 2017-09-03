FROM python:3.6.2-slim

ADD . /code
WORKDIR /code
RUN pip install -r ./data/installs.txt
CMD ["python", "app.py"]

