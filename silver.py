# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE guanjie_catalog.silver.customer
# MAGIC   TBLPROPERTIES (
# MAGIC     'delta.enableDeletionVectors' = 'false',
# MAGIC     'delta.enableIcebergCompatV2' = 'true',
# MAGIC     'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC     'delta.columnMapping.mode' = 'name'
# MAGIC   ) AS
# MAGIC   SELECT *, current_timestamp() AS load_timestamp FROM guanjie_catalog.bronze.customer;

# COMMAND ----------

# MAGIC %sql
# MAGIC   CREATE OR REPLACE TABLE guanjie_catalog.silver.lineitem
# MAGIC   TBLPROPERTIES (
# MAGIC     'delta.enableDeletionVectors' = 'false',
# MAGIC     'delta.enableIcebergCompatV2' = 'true',
# MAGIC     'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC     'delta.columnMapping.mode' = 'name'
# MAGIC   ) AS
# MAGIC   SELECT *, current_timestamp() AS load_timestamp FROM guanjie_catalog.bronze.lineitem;

# COMMAND ----------

# MAGIC %sql
# MAGIC   CREATE OR REPLACE TABLE guanjie_catalog.silver.nation
# MAGIC   TBLPROPERTIES (
# MAGIC     'delta.enableDeletionVectors' = 'false',
# MAGIC     'delta.enableIcebergCompatV2' = 'true',
# MAGIC     'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC     'delta.columnMapping.mode' = 'name'
# MAGIC   ) AS
# MAGIC  SELECT *, current_timestamp() AS load_timestamp FROM guanjie_catalog.bronze.nation;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC   CREATE OR REPLACE TABLE guanjie_catalog.silver.orders
# MAGIC   TBLPROPERTIES (
# MAGIC     'delta.enableDeletionVectors' = 'false',
# MAGIC     'delta.enableIcebergCompatV2' = 'true',
# MAGIC     'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC     'delta.columnMapping.mode' = 'name'
# MAGIC   ) AS
# MAGIC  SELECT *, current_timestamp() AS load_timestamp FROM guanjie_catalog.bronze.orders;

# COMMAND ----------

# MAGIC %sql
# MAGIC   CREATE OR REPLACE TABLE guanjie_catalog.silver.part
# MAGIC   TBLPROPERTIES (
# MAGIC     'delta.enableDeletionVectors' = 'false',
# MAGIC     'delta.enableIcebergCompatV2' = 'true',
# MAGIC     'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC     'delta.columnMapping.mode' = 'name'
# MAGIC   ) AS
# MAGIC  SELECT *, current_timestamp() AS load_timestamp FROM guanjie_catalog.bronze.part;

# COMMAND ----------

# MAGIC %sql
# MAGIC   CREATE OR REPLACE TABLE guanjie_catalog.silver.partsupp
# MAGIC   TBLPROPERTIES (
# MAGIC     'delta.enableDeletionVectors' = 'false',
# MAGIC     'delta.enableIcebergCompatV2' = 'true',
# MAGIC     'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC     'delta.columnMapping.mode' = 'name'
# MAGIC   ) AS
# MAGIC  SELECT *, current_timestamp() AS load_timestamp FROM guanjie_catalog.bronze.partsupp;

# COMMAND ----------

# MAGIC %sql
# MAGIC   CREATE OR REPLACE TABLE guanjie_catalog.silver.region
# MAGIC   TBLPROPERTIES (
# MAGIC     'delta.enableDeletionVectors' = 'false',
# MAGIC     'delta.enableIcebergCompatV2' = 'true',
# MAGIC     'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC     'delta.columnMapping.mode' = 'name'
# MAGIC   ) AS
# MAGIC   SELECT *, current_timestamp() AS load_timestamp FROM guanjie_catalog.bronze.region;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC   CREATE OR REPLACE TABLE guanjie_catalog.silver.supplier
# MAGIC   TBLPROPERTIES (
# MAGIC     'delta.enableDeletionVectors' = 'false',
# MAGIC     'delta.enableIcebergCompatV2' = 'true',
# MAGIC     'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC     'delta.columnMapping.mode' = 'name'
# MAGIC   ) AS
# MAGIC  SELECT *, current_timestamp() AS load_timestamp FROM guanjie_catalog.bronze.supplier;

# COMMAND ----------


