FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    build-essential \
    libcairo2 libcairo2-dev \
    libpango-1.0-0 libpango1.0-dev \
    libgdk-pixbuf-2.0-dev \
    libffi-dev \
    libjpeg-dev zlib1g-dev \
    shared-mime-info \
    libxml2 libxslt1.1 \
    pkg-config gcc python3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /app && chmod -R 777 /app

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 3000

CMD ["python", "manage.py", "runserver", "0.0.0.0:3000"]
