# NiFi-PostgreSQL-Elasticsearch Pipeline

This project implements a data pipeline using Apache NiFi to extract data from a PostgreSQL database, split each record into individual flowfiles, and load them into an Elasticsearch index.

## Overview

The NiFi data pipeline consists of three main processors:

1. **ExecuteSQLRecord**: This processor executes an SQL query against the PostgreSQL database and returns the result set as a Record. It is configured with the necessary connection details and SQL query to extract the desired data.

2. **SplitText**: After retrieving the data from the database, the SplitText processor is used to split each record into individual flowfiles. This processor is essential for breaking down the data into smaller units for further processing.

3. **PutElasticsearchHttp**: Once the data is split, the PutElasticsearchHttp processor is used to load each individual record into an Elasticsearch index. It is configured with the Elasticsearch cluster details and index information.

## Project Structure

```
NiFi-PostgreSQL-Elasticsearch-Pipeline/
│
├── templates/
│   ├── nifi-flow.xml
│   └── nifi-flow.json
│
├── screenshots/
│   ├── nifi_data_pipeline.png
│   └── elasticsearch_index_records.png
│
└── README.md   
```

## Usage

To use the NiFi data pipeline:

1. Import the NiFi flow template (`nifi-flow.xml`) into your NiFi instance.
2. Configure the processors (`ExecuteSQLRecord`, `SplitText`, `PutElasticsearchHttp`) with the appropriate settings for your environment (e.g., database connection details, Elasticsearch cluster information).
3. Start the NiFi flow to begin extracting data from the PostgreSQL database, splitting each record, and loading them into the Elasticsearch index.

## Screenshots

- [NiFi Data Pipeline](screenshots/nifi_data_pipeline.png)
- [Elasticsearch Index Records](screenshots/elasticsearch_index_records.png)

## License

This project is licensed under the [MIT License](LICENSE).
