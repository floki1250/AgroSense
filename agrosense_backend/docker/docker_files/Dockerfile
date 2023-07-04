# Use an official Python runtime as the base image
FROM python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory in the container
RUN mkdir /app

WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code into the container
COPY . /app/

# Expose the port that the application will run on
EXPOSE 8000

# Run the application
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
