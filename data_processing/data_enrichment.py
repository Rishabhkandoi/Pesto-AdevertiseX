from pyspark.sql import SparkSession
from pyspark.sql.functions import lit

# Initialize Spark session
spark = SparkSession.builder.appName("DataEnrichment").getOrCreate()

# Load the base data
data = spark.read.parquet("base_data.parquet")

# Enrich the data by adding a new column
enriched_data = data.withColumn("new_column", lit("enriched_value"))

# Save the enriched data to an output location
enriched_data.write.parquet("enriched_data.parquet")

# Stop Spark session
spark.stop()

