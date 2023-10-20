# Configuration File (config.json)

The `config.json` file contains configuration settings for different components of the project. You can customize these settings based on your environment and project requirements.

## Data Sources

- `ad_impressions_path`: Path to the ad impressions data source (e.g., JSON file).
- `clicks_conversions_path`: Path to the clicks and conversions data source (e.g., CSV file).
- `bid_requests_path`: Path to the bid requests data source (e.g., Avro file).

## Data Storage

- `output_path`: Path where processed data will be stored.

## Monitoring

- `prometheus_url`: URL for Prometheus for real-time monitoring.
- `grafana_url`: URL for Grafana to visualize data pipeline health.

Please customize the values in this file according to your project's environment and specific data source paths.

