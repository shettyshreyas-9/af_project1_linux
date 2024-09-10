from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago

# Define default_args
default_args = {
    'owner': 'airflow_SS',
    'retries': 1,
}

# Define the DAG
with DAG(
    'abc',
    default_args=default_args,
    description='An example DAG',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
) as dag:

    start = DummyOperator(
        task_id='start',
    )

    end = DummyOperator(
        task_id='end',
    )

    start >> end
