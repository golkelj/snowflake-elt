from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator

DBT_DIR = '/dbt'

default_args = {
    'owner': 'Jaden',
    'start_date': days_ago(1),
    'catchup': False
}

with DAG(
    dag_id='dbt_layered_run',
    schedule_interval=None,
    default_args=default_args,
    tags=['dbt']
) as dag:

    run_staging = BashOperator(
        task_id='run_staging_orders',
        bash_command=f'cd {DBT_DIR} && dbt run --select staging'
    )

    run_intermediate = BashOperator(
        task_id='run_intermediate',
        bash_command=f'cd {DBT_DIR} && dbt run --select int_order_items'
    )

    run_intermediate_summary = BashOperator(
        task_id='run_intermediate_summary',
        bash_command=f'cd {DBT_DIR} && dbt run --select int_order_items_summary'
    )

    run_marts = BashOperator(
        task_id='run_marts',
        bash_command=f'cd {DBT_DIR} && dbt run --select fct_orders'
    )

    run_tests = BashOperator(
        task_id='run_tests',
        bash_command=f'cd {DBT_DIR} && dbt test'
    )


    run_staging >> run_intermediate >> run_intermediate_summary >> run_marts >> run_tests
