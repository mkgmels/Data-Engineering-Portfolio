#imports
import datetime as dt
from datetime import timedelta as td
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
import pandas as pd

def clean_data():
	df=pd.read_csv("scooter.csv")
	df.columns=[x.lower() for x in df.columns]
	df.drop(columns='region_id',inplace=True)
	for col in ["started_at","ended_at"]:
		df[col] = pd.to_datetime(df[col],format="%m/%d/%Y %H:%M")
	df.to_csv("cleaned_scooters.csv")
