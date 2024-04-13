#imports
import datetime as dt
from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
import pandas as pd
import psycopg2 as db
from elasticsearch import Elasticsearch
from mydbdag_task1 import query_postgresql
from mydbdag_task2 import insert_elasticsearch

default_args={
'owner':'mkgmels73',
'start_date':dt.datetime(2024,4,12),
'retries':1,
'retry_delay':timedelta(minutes=2)
}




with DAG("Mydbdag",default_args=default_args,schedule_interval=timedelta(days=1)) as dag:
	get_data=PythonOperator(task_id="extract_postgresql",python_callable=query_postgresql)
	insert_data=PythonOperator(task_id="isnert_elasticsearch",python_callable=insert_elasticsearch)
	
	get_data >> insert_data
