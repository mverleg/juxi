
FROM python:3.10.15-alpine3.20

WORKDIR /code
EXPOSE 5000

COPY pyproject.toml ./

RUN pip install .

COPY . ./

ENTRYPOINT ["python3", "app.py"]

