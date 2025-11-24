# ===============================
# Stage 1 — Build dependencies
# ===============================
FROM python:3.13.9-slim AS builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
        libffi-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir --prefix=/install -r requirements.txt

# ===============================
# Stage 2 — Runtime
# ===============================
FROM python:3.13.9-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/install/bin:$PATH"

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libpq-dev \
        libffi-dev && \
    rm -rf /var/lib/apt/lists/*

COPY --from=builder /install /usr/local

COPY .. .
