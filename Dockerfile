FROM python:3.11-alpine

# Set project directory
ENV PROJECT_DIR=/app

WORKDIR ${PROJECT_DIR}

# Install dependencies
COPY requirements.txt ${PROJECT_DIR}
RUN pip install -r requirements.txt
RUN pip install gunicorn

# Copy source code
COPY ./src ${PROJECT_DIR}

EXPOSE 8000

# Execute gunicorn
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000"]
