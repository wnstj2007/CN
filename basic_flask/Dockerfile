FROM ubuntu:20.04

MAINTAINER Junseo "201802096@o.cnu.ac.kr"

RUN apt update -y && \
	apt install -y python3-pip python3-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "201802096_app.py" ]
