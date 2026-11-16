FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir torch==2.15.0 \
    --index-url https://download.pytorch.org/whl/cpu

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY database.py .
COPY distilbert_prediction.py .
COPY id_to_label.json .
COPY banking77_distilbert_final/ ./banking77_distilbert_final/

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
