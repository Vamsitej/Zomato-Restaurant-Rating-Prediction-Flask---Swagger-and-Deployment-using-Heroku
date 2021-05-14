# Dockerfile, Image, container
FROM tiangolo/uwsgi-nginx-flask:python3.6
WORKDIR /app/
COPY requirements.txt /app/
RUN pip install -r ./requirements.txt
COPY app2.py __init__.py /app/

