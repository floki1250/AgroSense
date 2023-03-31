FROM node:18-alpine

RUN mkdir /code
COPY . /code/
WORKDIR /code

RUN yarn && yarn cache clean
RUN yarn build

ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=3000

EXPOSE 3000

