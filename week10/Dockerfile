FROM node:12

MAINTAINER Junseo "201802096@o.cnu.ac.kr"

COPY ./package*.json /app/

WORKDIR /app

RUN npm install

COPY . /app

EXPOSE 3000

ENTRYPOINT [ "node" ]

CMD [ "201802096_server.js" ]
