FROM alpine:latest
LABEL mainter="ktokolwiek <someone@example.com>"
LABEL description="Apache ze stronka"
RUN apk add --update python
ADD serwer.py /
CMD ["python", "serwer.py"]

