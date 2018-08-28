FROM ubuntu:18.04
MAINTAINER Mario Kaack

RUN apt-get update && \
    apt-get install -y apache2 && \
    apt-get clean

COPY index.html style.css /var/www/html/

EXPOSE 80

VOLUME ["/var/www/html"]

ENTRYPOINT ["apachectl"]
CMD ["-D", "FOREGROUND"]

