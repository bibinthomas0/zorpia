FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/authentication
WORKDIR /app/authentication

COPY ./entrypoint.sh .

CMD ["gunicorn", "authentication.wsgi:application", "--bind", "0.0.0.0:8001"]
