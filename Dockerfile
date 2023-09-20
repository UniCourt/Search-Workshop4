FROM public.ecr.aws/docker/library/python:3.10

RUN apt-get update && apt-get install -y postgresql-client

RUN pip install psycopg2-binary

ENV POSTGRES_DB='amazon'
ENV POSTGRES_USER='workshop_user'

ENV POSTGRES_PASSWORD='workshop_user1'

ENV POSTGRES_HOST='127.0.0.1'
ENV POSTGRES_PORT='5435'
COPY ./requirements.txt /
RUN pip install -r ./requirements.txt

COPY . /
WORKDIR /src/app

EXPOSE 5000
ENV ES_HOST='127.0.0.1'
ENV ES_PORT=9200
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
