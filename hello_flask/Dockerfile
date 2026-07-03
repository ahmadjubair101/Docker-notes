FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    pkg-config \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/

RUN pip install --no-cache-dir flask mysqlclient

EXPOSE 5002

CMD ["python", "app.py"]



