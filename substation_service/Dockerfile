FROM python:3.10-slim
WORKDIR /app
COPY main.py .
RUN pip install flask prometheus_client
EXPOSE 5000 8000
CMD ["python", "main.py"]
