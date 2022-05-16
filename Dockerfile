# pull official base image
FROM python:3.10.4

# set working directory
WORKDIR /code

# set environment variablees
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install build dependencies
RUN apt-get update \
  && apt-get install -y netcat

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy docker-entrypoint.sh
COPY docker-entrypoint.sh .
RUN chmod +x docker-entrypoint.sh

# copy project
COPY . .

# run docker-entrypoint.sh
ENTRYPOINT ["./docker-entrypoint.sh"]
