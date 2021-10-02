FROM python:3.9-slim AS builder


COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

COPY . /app

# removing preexisting build files and creating a fresh build
RUN rm -rf ./app/_build/

WORKDIR /app


# added migrate command to move from old format
RUN jupyter-book toc migrate /app/_toc.yml -o /app/_toc.yml & jupyter-book build .

FROM nginx:alpine

COPY --from=builder /app/_build/html /usr/share/nginx/html/
COPY ./deploy/nginx.conf /etc/nginx/conf.d/default.conf
