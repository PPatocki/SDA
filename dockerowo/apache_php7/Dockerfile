FROM alpine:latest
LABEL mainter="ktokolwiek <someone@example.com>"
LABEL description="Docker with apacheand php7"
ENV PHPVERSION 7
RUN apk add --update apache2 php${PHPVERSION}-apache2 php${PHPVERSION} && \
rm -rf /var/cache/apk/* && \
rm -rf /run/apache2 && \
mkdir /run/apache2 && \
rm -rf /var/www/localhost/htdocs/index.html && \
echo "<?php phpinfo(); ?>" > /var/www/localhost/htdocs/index.php && \
chmod 755 /var/www/localhost/htdocs/index.php
#ADD files/moja_gra.php /var/www
EXPOSE 80/tcp
ENTRYPOINT ["httpd"]
CMD ["-D", "FOREGROUND"]
#COPY
#ADD
