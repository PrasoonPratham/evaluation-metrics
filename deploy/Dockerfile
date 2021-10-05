FROM python:3.9-slim AS builder

# Configure Pipenv for running in container
ENV PIP_NO_CACHE_DIR=false \
    POETRY_VIRTUALENVS_CREATE=false

# Get the dependencies ready
RUN apt-get -y update \
    && apt-get install git netcat -y \
    && rm -rf /root/.cache/pip/* \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install pipenv
RUN pip install -U poetry

# Define the working directory
WORKDIR /app

# Copy all the files, and get dependencies ready
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev

# Copy the source files
COPY . .

# Migrate using jupyter book
RUN jupyter-book toc migrate /app/_toc.yml -o /app/_toc.yml & jupyter-book build .

# Use nginx to deploy
FROM nginx:alpine

COPY --from=builder /app/_build/html /usr/share/nginx/html/
COPY ./deploy/nginx.conf /etc/nginx/conf.d/default.conf
