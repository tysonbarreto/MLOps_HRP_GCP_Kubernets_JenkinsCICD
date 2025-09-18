FROM python:3.11-slim-buster

ENV PYTHONWRITEBYTECODE=1 \
    PYTHONBUFFERED=1

WORKDIR /app

RUN apt-get update -y && apt-get upgrade -y && apt-get install -y --no-install-recommends\
    libgomp1 && apt-get clean && rm -rf /var/lib/apt/lists/*


COPY . .
RUN pip install --no-cache-dir requirements.txt

RUN dvc repro

EXPOSE 5000

CMD ["python","application.py"]