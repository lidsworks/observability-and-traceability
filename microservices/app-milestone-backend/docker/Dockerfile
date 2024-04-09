FROM python:3.9.18-slim-bookworm

RUN apt-get update && apt-get install -y python3-dev libevent-dev gcc

WORKDIR /src
COPY src/requirements.txt /src
RUN pip install -r requirements.txt
ADD src/. .

EXPOSE 5000

ENTRYPOINT ["newrelic-admin", "run-program"]
CMD ["flask", "run", "--host", "0.0.0.0"]