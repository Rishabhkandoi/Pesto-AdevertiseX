import json
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
from jsonschema import validate, ValidationError

# JSON schema for data validation
json_schema = {
    "type": "object",
    "properties": {
        "ad_id": {"type": "string"},
        "user_id": {"type": "string"},
        "timestamp": {"type": "string", "format": "date-time"},
        "website": {"type": "string"}
    },
    "required": ["ad_id", "user_id", "timestamp", "website"]
}

def validate_json_data(json_data):
    try:
        data = json.loads(json_data)
        validate(data, json_schema)
        return True, None  # Data is valid
    except ValidationError as e:
        error_message = f"Validation error: {e.message}"
        return False, error_message  # Data is invalid
    except Exception as ex:
        error_message = f"Error during validation: {str(ex)}"
        return False, error_message  # Error during validation

# Avro schema for Avro data validation
avro_schema = avro.schema.parse(open("your_avro_schema.avsc").read())

def validate_avro_data(avro_data):
    try:
        with open(avro_data, 'rb') as avro_file:
            reader = DataFileReader(avro_file, DatumReader(avro_schema))
            for record in reader:
                pass  # Do nothing, just read and validate
            return True, None  # Data is valid
    except Exception as ex:
        error_message = f"Validation error: {str(ex)}"
        return False, error_message  # Data is invalid

# Sample JSON data for validation
sample_json_data = """
{
    "ad_id": "ad123",
    "user_id": "user456",
    "timestamp": "2023-10-20T15:30:00Z",
    "website": "example.com"
}
"""

# Test JSON data validation
is_json_valid, json_validation_error = validate_json_data(sample_json_data)

if is_json_valid:
    print("JSON data is valid.")
else:
    print("JSON data is invalid.")
    print(f"Error: {json_validation_error}")

# Sample Avro data file for validation
sample_avro_data = "sample_avro_data.avro"

# Test Avro data validation
is_avro_valid, avro_validation_error = validate_avro_data(sample_avro_data)

if is_avro_valid:
    print("Avro data is valid.")
else:
    print("Avro data is invalid.")
    print(f"Error: {avro_validation_error}")

