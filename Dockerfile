# Use an official Python runtime as base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy necessary files
COPY requirements.txt requirements.txt
COPY src src

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Default command
CMD ["python", "src/ingestion.py"]
