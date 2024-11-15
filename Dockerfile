# Gunakan base image Python
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Salin file requirements.txt dan install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Salin semua file ke container
COPY . .

# Ekspos port untuk Flask
EXPOSE 8080

# Jalankan aplikasi Flask
CMD ["python", "app.py"]
