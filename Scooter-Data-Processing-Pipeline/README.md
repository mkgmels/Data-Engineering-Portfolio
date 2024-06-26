# Scooter Data Processing Pipeline

This project implements an Airflow data pipeline for processing and manipulating scooter data. The pipeline consists of three main tasks:

1. Loading the data into a Pandas DataFrame, cleaning it, and exporting it as a .csv file.
2. Loading the cleaned data into a Pandas DataFrame, filtering it by selecting the rows in a specific period, and exporting the filtered data to a .csv file.
3. Copying the data file from one directory to another.

## Project Structure

The project structure is organized as follows:

- **input_data**: Contains the input data file `scooters.csv`.
- **scripts**: Contains the Python scripts for data processing tasks.
  - `clean_data.py`: Script to load and clean the data.
  - `filter_data.py`: Script to filter the cleaned data.
  - `preprocess_data_dag.py`: Airflow DAG script defining the pipeline tasks.
- **logs**: Contains log files for each task execution.
  - `task1.log`: Log file for Task 1 execution.
  - `task2.log`: Log file for Task 2 execution.
  - `task3.log`: Log file for Task 3 execution.
- **screenshots**: Contains screenshots of the Airflow UI and DAG graph.
  - [DAG UI](screenshots/dag_ui.png): Screenshot of the Airflow UI showing the DAG.
  - [DAG Graph](screenshots/dag_graph.png): Screenshot of the DAG graph.
- **output_data**: Contains the output data files generated by the pipeline.
  - `cleaned_scooters.csv`: Output file from Task 1.
  - `filtered_scooters.csv`: Output file from Task 2.

## Usage

To run the data pipeline, follow these steps:

1. Ensure that Airflow is installed and configured.
2. Copy the contents of the `scripts` folder into the Airflow DAGs folder.
3. Start the Airflow webserver and scheduler.
4. Access the Airflow UI and enable the DAG `preprocess_data_dag`.
5. Trigger the DAG to start the pipeline execution.

## DAG Description

The `preprocess_data_dag` DAG orchestrates the execution of the three tasks:

1. Task 1 (`clean_data`): Loads the input data `scooters.csv` into a Pandas DataFrame, cleans it, and exports the cleaned data as `cleaned_scooters.csv`.
2. Task 2 (`filter_data`): Loads the cleaned data `cleaned_scooters.csv` into a Pandas DataFrame, filters it by selecting rows in a specific period, and exports the filtered data as `filtered_scooters.csv`.
3. Task 3 (`copy_data`): Copies the data file from the home directory to the Desktop.

## Logs

Log files for each task execution can be found in the `logs` folder. These log files provide detailed information about the execution of each task.

