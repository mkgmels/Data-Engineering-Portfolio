# Data Pipeline with Great Expectations Validation

## Overview

This project implements a data pipeline for performing data validations using the Great Expectations Python library. The pipeline is created using Apache NiFi, with various processors orchestrated to generate synthetic data, validate it against predefined expectations, process the validation results, and route them based on their outcome.

## Pipeline Components

### 1. StartPipeline Processor

- **Type:** GenerateFlowFile
- **Name:** StartPipeline
- **Purpose:** Generates an empty flowfile to trigger the start of the pipeline.

### 2. Generate1000Records Processor

- **Type:** ExecuteStreamCommand
- **Name:** Generate1000Records
- **Script:** `generate_fake_data.py`
- **Purpose:** Executes a Python script to generate synthetic data and load it into a `people.csv` file.

### 3. ValidatePeopleData Processor

- **Type:** ExecuteStreamCommand
- **Name:** ValidatePeopleData
- **Script:** `export_results.py`
- **Purpose:** Executes a Python script to create a Great Expectations context, call an installed expectations suite, run its validator against the data, and save the validation results into a `results.json` file.

### 4. ExecuteScript Processor

- **Type:** ExecuteScript
- **Name:** ExecuteScript
- **Script:** `peoplevalidationscript.py`
- **Purpose:** Executes a Python script to load the expectation results from `results.json`, perform processing on it, check if all expectation checks succeeded or not, and pass the final result to the next processor.

### 5. ExtractResultAttribute Processor

- **Type:** EvaluateJsonPath
- **Name:** ExtractResultAttribute
- **Purpose:** Extracts the result attribute and exports it as a flowfile attribute to the next processor.

### 6. RouteAnAttribute Processor

- **Type:** RouteAnAttribute
- **Name:** RouteBasedOnResult
- **Purpose:** Routes the result attribute based on its value (`"pass"` or `"fail"`) to the next processor.

### 7. LoadIntoDB Processor

- **Type:** PutFile
- **Name:** LoadIntoDB
- **Purpose:** Loads the final result into a text file. Can be replaced with any processor to further process the flowfiles based on its attribute value.

## Project Structure

- **data**: Folder containing input and output data.
  - `people.csv`: Synthetic input data file.
  - `results.json`: Validation results file.
  - **output_data**: Folder containing output text files.
- **data_validation_report**: Folder containing the HTML file showing the results of the `people.validation` suite expectations.
- **notebooks**: Folder containing Jupyter notebooks.
  - `datasource_new.ipynb`: Notebook for creating the Great Expectations datasource.
  - `edit_people.validation.ipynb`: Notebook containing code for configuring the `people.validation` expectation suite.
- **peoplepipeline**: Folder containing configuration files and scripts used by Great Expectations Python library.
- **screenshots**: Folder containing screenshots.
  - [age_column_level_expectations.png](screenshots/age_column_level_expectations.png): Results of expectations run against the "age" column.
  - [Data-Validation-Pipeline.png](screenshots/Data-Validation-Pipeline.png): NiFi pipeline screenshot.
  - [expectations_suite_overview.png](screenshots/expectations_suite_overview.png): Information related to the `people.validation` expectation suite.
  - [table_level_expectations.png](screenshots/table_level_expectations.png): Results of expectations run against the table of data.
- **scripts**: Folder containing Python scripts.
  - `export_results.py`
  - `generate_fake_data.py`
  - `peoplevalidationscript.py`
- **templates**: Folder containing NiFi template file.
  - `Data-Validation-Pipeline-Template.xml`: NiFi template file of the data pipeline.



