FROM python:3.6

# install dependencies
RUN apt-get update
RUN apt-get install -y mysql-server

#init database
WORKDIR /tmp
ADD ./docker_files/db/init.sql /tmp/init.sql
RUN find /var/lib/mysql -type f -exec touch {} \; && service mysql start && mysql -u root < init.sql

#install code
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

#run
EXPOSE 3306
EXPOSE 5000
CMD [ "./start.sh" ]
