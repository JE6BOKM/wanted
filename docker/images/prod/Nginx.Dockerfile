FROM nginx:alpine

COPY . ./code
WORKDIR /code

RUN rm /etc/nginx/conf.d/default.conf

COPY ./docker/images/prod/nginx.conf /etc/nginx/conf.d/default.conf
