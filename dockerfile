FROM apache/airflow:2.9.0-python3.11

# Switch to airflow user (this preserves the Airflow installation)
USER airflow

# Install dbt-snowflake (latest compatible version)
RUN pip install --no-cache-dir dbt-snowflake

# Switch back to root to copy volumes if needed (optional)
USER root

# Default working directory inside container
WORKDIR /opt/airflow
