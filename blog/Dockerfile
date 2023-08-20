FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt .
RUN ls -la
RUN pip install -r requirements.txt
COPY . /code/
