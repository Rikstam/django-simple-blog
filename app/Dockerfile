# pull official base image
FROM python:3.10-slim-buster

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
# RUN pip install --upgrade pip
#COPY ./requirements.txt .
RUN apt-get update \ 
    && apt-get -y install pipenv netcat gcc postgresql \
    && apt-get clean

COPY ./Pipfile .
COPY ./Pipfile.lock .
RUN pipenv install --system --deploy

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# add app
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]