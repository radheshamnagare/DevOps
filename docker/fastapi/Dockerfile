#base image
FROM ubuntu
#add api
ADD . /
#installation
RUN apt-get update
RUN apt-get install -y tzdata 	
RUN apt install -y postgresql postgresql-client
EXPOSE 5432
VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]
RUN su - postgres \
    service postgresql start

#psycopg2 dependency
RUN apt-get install -y python3  python3-pip python3-apt
RUN apt-get install libpq-dev -y

#install requirements
RUN pip3 install -r requirements.txt
EXPOSE 9000
CMD ["uvicorn","main:app ","--host","127.0.0.1","--port","9000"]


