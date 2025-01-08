FROM python:3.10-slim AS base

WORKDIR /app

COPY /src/main.py .
COPY /data_files/data.csv .
COPY /test ./tests
COPY requirements.txt .

ENV PYTHONPATH=/app
RUN pip install --no-cache-dir -r requirements.txt

FROM base AS test
RUN pip install pytest

EXPOSE 8080

CMD ["pytest"]

FROM base AS prod
CMD ["python", "main.py"]