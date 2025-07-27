ARG ENV

FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x /app/entrypoint.sh

RUN if [ "$ENV" = "prod" ]; then python3 manage.py collectstatic --no-input --hash; fi

ENTRYPOINT ["/app/entrypoint.sh"]
