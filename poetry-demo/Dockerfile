# Stage 1: Use the NATS Server image directly
FROM nats:latest as nats_server

# Stage 2: Build your Python application image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Pyproject.toml and poetry.lock files into the container
COPY pyproject.toml poetry.lock ./

# Install Poetry and project dependencies
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi

# Copy your Python application code into the container
COPY . .

# Install tox for running tests
RUN pip install --no-cache-dir tox

# Copy NATS Server binary from the NATS Server image
COPY --from=nats_server /nats-server /usr/local/bin/

# Define the command to run your Python application
CMD ["python", "poetry_demo/calc_server.py", "--nats-port", "4222"]
