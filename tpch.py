# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE guanjie_catalog.tpch.customer
# MAGIC   TBLPROPERTIES (
# MAGIC     'delta.enableDeletionVectors' = 'false',
# MAGIC     'delta.enableIcebergCompatV2' = 'true',
# MAGIC     'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC     'delta.columnMapping.mode' = 'name'
# MAGIC   ) AS
# MAGIC   SELECT * FROM samples.tpch.customer;

# COMMAND ----------

# MAGIC %sql
# MAGIC   CREATE OR REPLACE TABLE guanjie_catalog.tpch.lineitem
# MAGIC   TBLPROPERTIES (
# MAGIC     'delta.enableDeletionVectors' = 'false',
# MAGIC     'delta.enableIcebergCompatV2' = 'true',
# MAGIC     'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC     'delta.columnMapping.mode' = 'name'
# MAGIC   ) AS
# MAGIC   SELECT * FROM samples.tpch.lineitem;

# COMMAND ----------

# MAGIC %sql
# MAGIC   CREATE OR REPLACE TABLE guanjie_catalog.tpch.nation
# MAGIC   TBLPROPERTIES (
# MAGIC     'delta.enableDeletionVectors' = 'false',
# MAGIC     'delta.enableIcebergCompatV2' = 'true',
# MAGIC     'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC     'delta.columnMapping.mode' = 'name'
# MAGIC   ) AS
# MAGIC   SELECT * FROM samples.tpch.nation;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC   CREATE OR REPLACE TABLE guanjie_catalog.tpch.orders
# MAGIC   TBLPROPERTIES (
# MAGIC     'delta.enableDeletionVectors' = 'false',
# MAGIC     'delta.enableIcebergCompatV2' = 'true',
# MAGIC     'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC     'delta.columnMapping.mode' = 'name'
# MAGIC   ) AS
# MAGIC   SELECT * FROM samples.tpch.orders;

# COMMAND ----------

# MAGIC %sql
# MAGIC   CREATE OR REPLACE TABLE guanjie_catalog.tpch.part
# MAGIC   TBLPROPERTIES (
# MAGIC     'delta.enableDeletionVectors' = 'false',
# MAGIC     'delta.enableIcebergCompatV2' = 'true',
# MAGIC     'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC     'delta.columnMapping.mode' = 'name'
# MAGIC   ) AS
# MAGIC   SELECT * FROM samples.tpch.part;

# COMMAND ----------

# MAGIC %sql
# MAGIC   CREATE OR REPLACE TABLE guanjie_catalog.tpch.partsupp
# MAGIC   TBLPROPERTIES (
# MAGIC     'delta.enableDeletionVectors' = 'false',
# MAGIC     'delta.enableIcebergCompatV2' = 'true',
# MAGIC     'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC     'delta.columnMapping.mode' = 'name'
# MAGIC   ) AS
# MAGIC   SELECT * FROM samples.tpch.partsupp;

# COMMAND ----------

# MAGIC %sql
# MAGIC   CREATE OR REPLACE TABLE guanjie_catalog.tpch.region
# MAGIC   TBLPROPERTIES (
# MAGIC     'delta.enableDeletionVectors' = 'false',
# MAGIC     'delta.enableIcebergCompatV2' = 'true',
# MAGIC     'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC     'delta.columnMapping.mode' = 'name'
# MAGIC   ) AS
# MAGIC   SELECT * FROM samples.tpch.region;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC   CREATE OR REPLACE TABLE guanjie_catalog.tpch.supplier
# MAGIC   TBLPROPERTIES (
# MAGIC     'delta.enableDeletionVectors' = 'false',
# MAGIC     'delta.enableIcebergCompatV2' = 'true',
# MAGIC     'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC     'delta.columnMapping.mode' = 'name'
# MAGIC   ) AS
# MAGIC   SELECT * FROM samples.tpch.supplier;
