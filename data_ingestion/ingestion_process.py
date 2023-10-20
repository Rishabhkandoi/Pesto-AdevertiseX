# Example code for ingesting JSON, CSV, and Avro data

import json
import csv
from avro.datafile import DataFileReader
from avro.io import DatumReader

def ingest_impressions(json_file):
    with open(json_file, 'r') as f:
        impressions_data = json.load(f)
    return impressions_data

def ingest_clicks_conversions(csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        clicks_conversions_data = [row for row in reader]
    return clicks_conversions_data

def ingest_bid_requests(avro_file):
    with open(avro_file, 'rb') as f:
        reader = DataFileReader(f, DatumReader())
        bid_requests_data = [record for record in reader]
    return bid_requests_data

# Example usage
impressions_data = ingest_impressions('sample_data/impressions.json')
clicks_conversions_data = ingest_clicks_conversions('sample_data/clicks_conversions.csv')
bid_requests_data = ingest_bid_requests('sample_data/bid_requests.avro')

