FROM ubuntu:16.04

# install dependencies
RUN sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
RUN apt-get update \
    && apt-get install -y apt-utils \                                           
    && { \
        echo debconf debconf/frontend select Noninteractive; \
        echo mysql-community-server mysql-community-server/data-dir \
            select ''; \
        echo mysql-community-server mysql-community-server/root-pass \
            password ''; \
        echo mysql-community-server mysql-community-server/re-root-pass \
            password ''; \
        echo mysql-community-server mysql-community-server/remove-test-db \
            select true; \
    } | debconf-set-selections \
    && apt-get install -y mysql-server python3 python3-pip

#init database
WORKDIR /tmp
ADD ./docker_files/db/init.sql /tmp/init.sql
RUN find /var/lib/mysql -type f -exec touch {} \; && service mysql start && mysql -u root < init.sql

#install code
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt

#run
EXPOSE 3306
EXPOSE 5000
CMD [ "./start.sh" ]
