
FROM python:3.10.15-alpine3.20

EXPOSE 8080
WORKDIR /code

COPY pyproject.toml ./

RUN pip install .

COPY . ./

# https://flask.palletsprojects.com/en/stable/tutorial/deploy/
ENTRYPOINT ["waitress-serve", "--call", "app:create_app"]

