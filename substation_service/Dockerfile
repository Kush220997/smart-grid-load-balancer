FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install flask prometheus_client
CMD ["python", "main.py"]