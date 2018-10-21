FROM python:3-alpine
LABEL maintainer="John Louis Del Rosario <john2x@gmail.com>"

COPY ./app /app
WORKDIR /app
ENV PYTHONPATH /app

RUN pip install -r /app/requirements.txt

COPY start.sh /start.sh
RUN chmod +x /start.sh

CMD ["/start.sh"]