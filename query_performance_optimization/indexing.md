# Indexing

## Indexing in Storage Systems

Creating indexes in storage systems can significantly improve query performance. Consider the following options for indexing:

- **Hive:** Hive supports the creation of indexes to accelerate query execution. Indexing frequently queried columns can reduce the time needed for filtering and sorting operations.

- **Parquet:** Parquet file format allows for predicate pushdown, which serves as an implicit form of indexing. By structuring data efficiently and using appropriate column encoding, Parquet can enhance query performance.

## Spark SQL Indexing

Spark SQL provides the ability to create and use indexes for dataframes. Indexing is beneficial for large datasets to speed up data retrieval operations.

Use the `createOrReplaceTempView` method to create a temporary view of your dataframe and then create an index using `createIndex` to optimize query performance.


