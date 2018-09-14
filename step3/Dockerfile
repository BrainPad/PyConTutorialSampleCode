from python:3.6

copy requirements.txt /code/requirements.txt

workdir /code

run pip install -r requirements.txt

copy ./samplebot /code/samplebot

cmd ["python", "samplebot/run.py"]
