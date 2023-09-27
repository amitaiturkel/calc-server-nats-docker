# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Pyproject.toml and poetry.lock files into the container
COPY pyproject.toml poetry.lock ./

# Install Poetry and project dependencies
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi

# Copy your Calc server code into the container
COPY . .

# Expose any ports that your Calc server needs (if any)
EXPOSE 12345

# Install NATS Server inside the container (example, you may need to adjust this)
RUN wget https://github.com/nats-io/nats-server/releases/download/v2.6.4/nats-server-v2.6.4-linux-amd64.zip && \
    unzip nats-server-v2.6.4-linux-amd64.zip && \
    mv nats-server-v2.6.4-linux-amd64/nats-server /usr/local/bin/ && \
    rm -rf nats-server-v2.6.4-linux-amd64.zip nats-server-v2.6.4-linux-amd64

# Copy your tests directory into the container
COPY tests/ tests/

# Install tox for running tests
RUN pip install --no-cache-dir tox

# Define the command to run your Calc server
CMD ["python", "poetry_demo/calc_server.py", "--nats-port", "4222"]
