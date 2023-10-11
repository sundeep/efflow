# Use an official Python runtime as the parent image
FROM python:3.9-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the Docker container
WORKDIR /api

# Copy the current directory into the container at /app
COPY . /api/

# Install required packages
RUN pip install --upgrade pip && pip install -r requirements.txt

# Specify the command to run on container start
CMD ["uvicorn", "api.api:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
