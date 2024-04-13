#imports
import datetime as dt
from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
import pandas as pd
import psycopg2 as db
from elasticsearch import Elasticsearch

def insert_elasticsearch():
	es=Elasticsearch()
	df=pd.read_csv("postgresql_data.csv")
	for i,r in df.iterrows():
		doc=r.to_json()
		res=es.index(index="frompostgresql",doc_type="doc",body=doc)
		print(res)
