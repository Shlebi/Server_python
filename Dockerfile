FROM python:3.9-slim

#Рабочая директория в конейнере
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]