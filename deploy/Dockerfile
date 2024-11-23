
FROM 3.10.15-slim-bullseye

RUN pip install .

WORKDIR /code
EXPOSE 5000

COPY . ./

CMD ["python3", "server.py"]
