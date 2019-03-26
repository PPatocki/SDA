FROM alpine:latest
LABEL mainter="ktokolwiek <someone@example.com>"
LABEL description="Doom in flash"
RUN apk add --update apache2 && \
rm -rf /var/cache/apk/* && \
rm -rf /run/apache2 && \
mkdir /run/apache2 && \
rm -rf /var/www/localhost/htdocs/index.html
COPY files/index.html /var/www/localhost/htdocs/
COPY files/doom.swf /var/www/localhost/htdocs/
EXPOSE 80/tcp
ENTRYPOINT ["httpd"]
CMD ["-D", "FOREGROUND"]
