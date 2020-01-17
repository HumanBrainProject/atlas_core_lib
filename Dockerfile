FROM python:3.7-alpine

ADD . /atlas-core-lib
WORKDIR /atlas-core-lib

RUN pip install -r requirements.txt

CMD ["python3 -m unittest"]
