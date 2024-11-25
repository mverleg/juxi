
FROM node:alpine3.20 AS static

COPY package.json ./

RUN npm install

FROM python:3.10.15-alpine3.20

EXPOSE 5000
WORKDIR /code

COPY ../pyproject.toml ./

RUN pip install .

COPY . ./

# https://flask.palletsprojects.com/en/stable/tutorial/deploy/
ENTRYPOINT ["waitress-serve", "--port", "5000", "--call", "app:create_app"]

