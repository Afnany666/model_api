FROM python:3.9-slim

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENV PORT 8080
EXPOSE 8080

CMD ["python", "app.py"]
