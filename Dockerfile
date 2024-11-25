
FROM node:alpine3.20 AS static

WORKDIR /code

COPY package.json ./
RUN npm install

COPY tailwind/ ./tailwind
RUN npx tailwindcss -i ./tailwind/juxi.css -o ./out/static/juxi.min.css --minify

FROM python:3.10.15-alpine3.20

EXPOSE 5000
WORKDIR /code

COPY pyproject.toml ./
RUN pip install .

COPY --from=static /code/node_modules/ ./node_modules
COPY --from=static /code/out/ ./out

COPY manage.py settings.py juxi ./

RUN printf '\n\nthrow Exception('local settings file should be mounted!')\n\n' > local.py

#TODO @mark: collect static

#TODO @mark: migrate on startup
ENTRYPOINT ["waitress-serve", "--port", "5000", "--call", "app:create_app"]

