FROM python:3.9 as requirements-stage

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes --dev


FROM python:3.9
ENV PYTHONUNBUFFERED 1

COPY --from=requirements-stage /tmp/requirements.txt /requirements.txt


RUN pip install --no-cache-dir --upgrade -r /requirements.txt

# Adds our application code to the image
COPY . /code
WORKDIR /code

EXPOSE 8000

# Run the production server
CMD newrelic-admin run-program gunicorn --bind 0.0.0.0:$PORT --access-logfile - config.wsgi:application
