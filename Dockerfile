FROM python:3.11

# Set the working directory to /app
WORKDIR /app

# Basic environment setup
RUN pip install --upgrade pip
RUN pip install Flask

# Copy the current directory contents into the container at /app
COPY ./src /app

# Make port 80 available to the world outside this container
EXPOSE 80

CMD [ "python", "app.py" ]
