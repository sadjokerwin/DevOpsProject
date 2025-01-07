FROM python:3.10-slim AS base

WORKDIR /app

COPY /src/main.py .
COPY /data_files/data.csv .
COPY /test ./tests

ENV PYTHONPATH=/app

FROM base AS test
RUN pip install pytest
CMD ["pytest"]

FROM base AS prod
CMD ["python", "main.py"]