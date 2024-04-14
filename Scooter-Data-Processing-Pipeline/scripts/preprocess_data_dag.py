#imports
import datetime as dt
from datetime import timedelta as td
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from clean_data import clean_data
from filter_data import filter_data
import pandas as pd

default_args={"owner":"mkgmels","start_date":dt.datetime(2024,4,13),"retries":1,"retry_delay":td(minutes=2)}

with DAG("preprocess_data_dag",default_args=default_args,schedule_interval=td(days=1)) as dag:
	task1 = PythonOperator(task_id="clean_data",python_callable=clean_data)
	task2 = PythonOperator(task_id="filter_data",python_callable=filter_data)
	task3 = BashOperator(task_id = "copy_data",bash_command = "cp /home/mohamed/filtered_scooters.csv /home/mohamed/Desktop")
	
	task1 >> task2 >> task3
