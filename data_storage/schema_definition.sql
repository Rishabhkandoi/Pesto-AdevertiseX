-- Schema Definition for Structured Data Using Apache Avro

-- Define an Avro schema for your structured data
CREATE SCHEMA StructuredDataSchema
  NAMESPACE 'com.example'
  TYPE RECORD
  NAME 'StructuredData'
  FIELDS (
    { "name": "field1", "type": "string" },
    { "name": "field2", "type": "int" },
    { "name": "field3", "type": "double" },
    { "name": "field4", "type": "string" }
  );

-- You can define more fields as needed

-- Register the schema with Avro for use in data serialization/deserialization
CREATE TABLE StructuredDataTable
  STORED AS AVRO
  TBLPROPERTIES (
    'avro.schema.literal' = '
      {
        "type": "record",
        "name": "StructuredData",
        "fields": [
          {"name": "field1", "type": "string"},
          {"name": "field2", "type": "int"},
          {"name": "field3", "type": "double"},
          {"name": "field4", "type": "string"}
          -- Define more fields here if needed
        ]
      }'
  );

