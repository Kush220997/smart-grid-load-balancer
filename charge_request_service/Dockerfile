FROM python:3.10-slim
WORKDIR /app
COPY main.py .
RUN pip install flask requests
EXPOSE 6000
CMD ["python", "main.py"]
