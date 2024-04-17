# SeeClickFix Data Pipeline with Apache NiFi, Elasticsearch, and Kibana

## Overview
This project aims to create a robust data pipeline using Apache NiFi to extract data from the SeeClickFix website, load it into an Elasticsearch index, and create a comprehensive Kibana dashboard for data visualization and analysis. The pipeline automates the extraction and transformation processes, providing real-time insights into issues reported on SeeClickFix within Bernalillo County.

## Project Structure
```
|-- extracted_data/
|   |-- Top_5_request_titles.csv
|   |-- records_count_per_day_created_at.csv
|-- links/
|   |-- link_to_scf_dashboard.txt
|-- screenshots/
|   |-- scfNifiFlow.png
|   |-- scf-Dashboard.png
|-- scripts/
|   |-- AddCoordinatesProcessor.py
|   |-- GetEveryPageProcessor.py
|   |-- QueryscfArchivedProcessor.py
|   |-- QueryscfProcessor.py
|-- templates/
|   |-- scfNifiFlowTemplate.xml
|   |-- scfNifiFlow.json
|-- README.md
```

## Files Description

1. **extracted_data/:** Contains statistics data files in the project, including CSV files containing top request titles and records count per day, which are extracted from the SeeClickFix Elasticsearch index using Kibana.

2. **links/:** Contains a text file (`link_to_scf_dashboard.txt`) providing a link to the SeeClickFix dashboard.

3. **screenshots/:** Contains screenshots of the NiFi data flow and the Kibana dashboard for reference and documentation purposes.

4. **scripts/:** Contains Python scripts used by Apache NiFi processors for various tasks such as querying SeeClickFix data, adding coordinates, etc.

5. **templates/:** Holds NiFi flow templates in both XML and JSON formats for easy import and deployment in Apache NiFi.

## Project Components

1. **Apache NiFi Data Pipeline:** This project utilizes Apache NiFi to construct a robust data pipeline for extracting data from the SeeClickFix website, loading it into an Elasticsearch index, and constructing a Kibana dashboard for comprehensive data visualization and analysis.

2. **Data Extraction:** The NiFi data flow begins with a Generate FlowFile processor, generating an empty flow file to initiate the pipeline. Subsequently, an ExecuteScript processor executes a custom Python script (`QueryscfProcessor.py`) to query the SeeClickFix issues data, extracting relevant information from the website.

3. **Data Transformation:** Following extraction, the SplitJson processor is employed to partition the extracted data into individual flow files, facilitating parallel processing and efficient handling of the dataset. Additionally, another ExecuteScript processor is utilized to add coordinates to the data, conforming to NiFi's geo_point data type requirements, enabling seamless integration with Kibana's mapping capabilities.

4. **Data Enrichment:** The EvaluateJsonPath processor is leveraged to generate unique identifiers for each flow file, acting as the equivalent of a primary key in Elasticsearch. This ensures that each record within the dataset possesses a distinct identifier, facilitating efficient indexing and retrieval.

5. **Data Loading:** Finally, the PutElasticsearchHttp processor is employed to load the processed flow files into an Elasticsearch index named "scf," enabling efficient storage and retrieval of the data. This step completes the data pipeline, ensuring that the extracted data is readily available for analysis and visualization within the Elasticsearch environment.

This comprehensive data pipeline seamlessly integrates data extraction, transformation, enrichment, and loading processes, enabling efficient handling and analysis of SeeClickFix data within the Elasticsearch and Kibana ecosystem.
