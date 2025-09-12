# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY src/ ./src/

#Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
RUN pip install pytest

# Default command to run tests
CMD ["pytest", "src/tests"]
