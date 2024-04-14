#imports
import datetime as dt
from datetime import timedelta as td
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
import pandas as pd

def filter_data():
	cleaned_df=pd.read_csv("cleaned_scooters.csv")
	start_date="2019-05-23"
	end_date="2019-05-28"
	filtered_df=cleaned_df[(cleaned_df["started_at"] > start_date) & (cleaned_df["started_at"] < end_date)]
	filtered_df.to_csv("filtered_scooters.csv")
	
