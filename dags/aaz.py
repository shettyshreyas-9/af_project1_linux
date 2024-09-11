from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
import os
from airflow.utils.dates import days_ago


# Define default arguments for the DAG
default_args = {
    'owner': 'airflow_SS',
    'start_date': days_ago(1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


# Define the DAG
with DAG(
    dag_id='apache_beam_etl_pipeline',
    default_args=default_args,
    schedule_interval='@daily',  # Adjust the schedule as needed
    catchup=False,
) as dag:
    
    
    run_beam_pipeline2 = BashOperator(
        task_id='run_beam_pipeline2',
        bash_command='python3 ~/airflow_projects/project1/beam_scripts/etl_pipe_1.py',  # Update path accordingly
    )
    

    # run_beam_pipeline4 = BashOperator(
    #     task_id='run_beam_pipeline4',
    #     bash_command='python3 /home/sst7260/airflow_projects/project1/beam_scripts/etl_pipe_1.py',  # Update path accordingly
    # )


    # Task to check the working directory
    check_dir_task = BashOperator(
        task_id='check_working_directory',
        bash_command='pwd',
    )
    

    
