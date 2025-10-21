# dockerfile
FROM apache/airflow:2.9.0-python3.11

# Switch to root to install dependencies
USER root

# Set default working directory inside container
WORKDIR /opt/airflow

# Copy requirements.txt into the container
COPY requirements.txt .

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Switch back to airflow user
USER airflow

