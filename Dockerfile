FROM python:3.11-slim

WORKDIR /app

# instalamos dependencias del sistema
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# instalamos dependencias de python
COPY pyproject.toml .
RUN pip install --no-cache-dir -e .

# copiamos el código
COPY . .

# creamos directorio de static files
RUN mkdir -p staticfiles media

# exponemos el puerto
EXPOSE 8000

# comando por defecto
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
