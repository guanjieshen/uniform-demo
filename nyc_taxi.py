# Databricks notebook source
# MAGIC %sql
# MAGIC   CREATE OR REPLACE TABLE guanjie_catalog.nyctaxi.trips
# MAGIC   TBLPROPERTIES (
# MAGIC     'delta.enableDeletionVectors' = 'false',
# MAGIC     'delta.enableIcebergCompatV2' = 'true',
# MAGIC     'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC     'delta.columnMapping.mode' = 'name'
# MAGIC   ) AS
# MAGIC   SELECT * FROM samples.nyctaxi.trips;
