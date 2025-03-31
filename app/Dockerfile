FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBITECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "my_project.wsgi:application"]