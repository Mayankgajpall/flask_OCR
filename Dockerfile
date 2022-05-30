FROM python:3.8.13-buster

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

ARG OCR_KEY
ENV OCR_KEY=${OCR_KEY}

EXPOSE 5000

CMD ["python", "ocr.py"]