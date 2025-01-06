FROM python:3.10-slim

WORKDIR /app

COPY /src/main.py /app
COPY /data_files/data.csv /app

CMD ["python", "main.py"]