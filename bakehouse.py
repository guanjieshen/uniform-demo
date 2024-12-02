# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE guanjie_catalog.bakehouse.media_gold_reviews_chunked
# MAGIC TBLPROPERTIES (
# MAGIC   'delta.enableDeletionVectors' = 'false',
# MAGIC   'delta.enableIcebergCompatV2' = 'true',
# MAGIC   'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC   'delta.columnMapping.mode' = 'name'
# MAGIC ) AS
# MAGIC SELECT * FROM samples.bakehouse.media_gold_reviews_chunked;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE guanjie_catalog.bakehouse.media_gold_reviews_chunked
# MAGIC TBLPROPERTIES (
# MAGIC   'delta.enableDeletionVectors' = 'false',
# MAGIC   'delta.enableIcebergCompatV2' = 'true',
# MAGIC   'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC   'delta.columnMapping.mode' = 'name'
# MAGIC ) AS
# MAGIC SELECT * FROM samples.bakehouse.media_gold_reviews_chunked;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE guanjie_catalog.bakehouse.sales_customers
# MAGIC TBLPROPERTIES (
# MAGIC   'delta.enableDeletionVectors' = 'false',
# MAGIC   'delta.enableIcebergCompatV2' = 'true',
# MAGIC   'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC   'delta.columnMapping.mode' = 'name'
# MAGIC ) AS
# MAGIC SELECT * FROM samples.bakehouse.sales_customers;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE guanjie_catalog.bakehouse.sales_franchises
# MAGIC TBLPROPERTIES (
# MAGIC   'delta.enableDeletionVectors' = 'false',
# MAGIC   'delta.enableIcebergCompatV2' = 'true',
# MAGIC   'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC   'delta.columnMapping.mode' = 'name'
# MAGIC ) AS
# MAGIC SELECT * FROM samples.bakehouse.sales_franchises;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE guanjie_catalog.bakehouse.sales_transactions
# MAGIC TBLPROPERTIES (
# MAGIC   'delta.enableDeletionVectors' = 'false',
# MAGIC   'delta.enableIcebergCompatV2' = 'true',
# MAGIC   'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC   'delta.columnMapping.mode' = 'name'
# MAGIC ) AS
# MAGIC SELECT * FROM samples.bakehouse.sales_transactions;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE guanjie_catalog.bakehouse.sales_suppliers
# MAGIC TBLPROPERTIES (
# MAGIC   'delta.enableDeletionVectors' = 'false',
# MAGIC   'delta.enableIcebergCompatV2' = 'true',
# MAGIC   'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC   'delta.columnMapping.mode' = 'name'
# MAGIC ) AS
# MAGIC SELECT * FROM samples.bakehouse.sales_suppliers;
