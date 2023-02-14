FROM python:3.11

# Basic environment setup
RUN pip install --upgrade pip
RUN pip install pipenv

ENV PROJECT_DIR=/app

# Set the working directory to specified path
WORKDIR ${PROJECT_DIR}

COPY Pipfile* ${PROJECT_DIR}
RUN pipenv install --system --deploy

# Copy source code directory to container
COPY ./src ${PROJECT_DIR}

# Make port 5000 available to the world outside this container
EXPOSE 5000

CMD [ "flask", "--app", "app", "run", "--host=0.0.0.0" ]
