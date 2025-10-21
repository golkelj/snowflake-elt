from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

# 1️⃣ Define a Python function to run
def hello_world():
    print("Hello, Airflow!")
    
def jaden():
    print("Hello, jaden!")

def goelkel():
    print("Hello, goelkel!")


# 2️⃣ Define the DAG
with DAG(
    dag_id='hello_airflow',             # Unique DAG ID
    start_date=datetime(2025, 10, 20),  # When to start scheduling
    schedule_interval=None,         # Run once per day
    catchup=False                        # Don't backfill old runs
) as dag:

    # 3️⃣ Define tasks
    task1 = PythonOperator(
        task_id='say_hello',
        python_callable=hello_world
    )
    
    task2 = PythonOperator(
        task_id='task_two',
        python_callable=jaden
    )
    
    task3 = PythonOperator(
        task_id='task_three',
        python_callable=goelkel
    ) 

# 4️⃣ Set task dependencies (optional)
task1 >> task2 >> task3
