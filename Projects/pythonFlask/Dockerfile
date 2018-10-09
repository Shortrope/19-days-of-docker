FROM alpine:3.8
MAINTAINER Mario Kaack
RUN apk add --no-cache python3  && \
    pip3 install --upgrade pip  && \
    pip3 install flask

EXPOSE 5000
COPY ./app /app
ENTRYPOINT ["python3", "/app/app.py"]