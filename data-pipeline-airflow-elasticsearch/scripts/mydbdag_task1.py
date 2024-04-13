#imports
import datetime as dt
from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
import pandas as pd
import psycopg2 as db
from elasticsearch import Elasticsearch

def query_postgresql():
	conn_string = "dbname='dataengineering' host='localhost' user='postgres' password='postgres'"
	conn=db.connect(conn_string)
	df=pd.read_sql("select name,city from people",conn)
	df.to_csv("postgresql_data.csv")
	print("-------Data saved-------")
