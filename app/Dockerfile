# pull official base image
FROM python:3.11.0b1-slim-buster

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
# RUN pip install --upgrade pip
#COPY ./requirements.txt .
RUN apt-get update \ 
    && apt-get -y install pipenv curl netcat gcc postgresql \
    && apt-get clean

COPY ./Pipfile .
COPY ./Pipfile.lock .
RUN pipenv install --system --deploy

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# add app
COPY . .

# Install Tailwind cli so there is no need for node.js
#RUN curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-linux-x64 \
#    && chmod +x tailwindcss-linux-x64 \
#    && mv tailwindcss-linux-x64 tailwindcss
# ./tailwindcss -i static/src/app.css -o static/dist/app.css --watch
# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]