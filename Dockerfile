FROM python:3.10-slim AS base

WORKDIR /app

COPY /src/main.py /app
COPY /data_files/data.csv /app
COPY /test/ ./tests

FROM base AS test
RUN pip install pytest
CMD ["pytest", "-s"]

FROM base AS prod
CMD ["python", "main.py"]