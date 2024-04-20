import json
import logging
import datetime
import pandas as pd
import great_expectations as gx
import great_expectations.jupyter_ux
from great_expectations.core.batch import BatchRequest
from great_expectations.checkpoint import SimpleCheckpoint
from great_expectations.exceptions import DataContextError
from great_expectations import DataContext

# Set the logging level to WARNING
logging.getLogger("great_expectations").setLevel(logging.WARNING)

context = gx.get_context()
suite = context.get_expectation_suite("people.validation")
batch_request = {'datasource_name': 'my_datasource', 'data_connector_name': 'default_inferred_data_connector_name', 'data_asset_name': 'people.csv', 'limit': 1000}
expectation_suite_name = "people.validation"
validator = context.get_validator(
    batch_request=BatchRequest(**batch_request),
    expectation_suite_name=expectation_suite_name
)

results = validator.validate()


# Define the output file path
output_file_path = "/home/mohamed/peoplepipeline/results.json"

# Write the results to a JSON file
with open(output_file_path, 'w') as output_file:
    json.dump(str(results), output_file,indent=1)

