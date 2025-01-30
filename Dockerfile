# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

LABEL maintainer="Yashasvi Matta"

# Copy the current directory contents into the container at /app
COPY ./src /app/src
COPY requirements.txt /app/
COPY .env /app/
COPY archive/ratings_small.csv /app/archive/

# Install the dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt


# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run the application
CMD ["python", "/app/src/app.py"]
