# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE guanjie_catalog.accuweather.forecast_daily_calendar_imperial
# MAGIC TBLPROPERTIES (
# MAGIC   'delta.enableDeletionVectors' = 'false',
# MAGIC   'delta.enableIcebergCompatV2' = 'true',
# MAGIC   'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC   'delta.columnMapping.mode' = 'name'
# MAGIC ) AS
# MAGIC SELECT * FROM samples.accuweather.forecast_daily_calendar_imperial;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE guanjie_catalog.accuweather.forecast_daily_calendar_metric
# MAGIC TBLPROPERTIES (
# MAGIC   'delta.enableDeletionVectors' = 'false',
# MAGIC   'delta.enableIcebergCompatV2' = 'true',
# MAGIC   'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC   'delta.columnMapping.mode' = 'name'
# MAGIC ) AS
# MAGIC SELECT * FROM samples.accuweather.forecast_daily_calendar_metric;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE guanjie_catalog.accuweather.forecast_daynight_imperial
# MAGIC TBLPROPERTIES (
# MAGIC   'delta.enableDeletionVectors' = 'false',
# MAGIC   'delta.enableIcebergCompatV2' = 'true',
# MAGIC   'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC   'delta.columnMapping.mode' = 'name'
# MAGIC ) AS
# MAGIC SELECT * FROM samples.accuweather.forecast_daynight_imperial;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE guanjie_catalog.accuweather.forecast_daynight_metric
# MAGIC TBLPROPERTIES (
# MAGIC   'delta.enableDeletionVectors' = 'false',
# MAGIC   'delta.enableIcebergCompatV2' = 'true',
# MAGIC   'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC   'delta.columnMapping.mode' = 'name'
# MAGIC ) AS
# MAGIC SELECT * FROM samples.accuweather.forecast_daynight_metric;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE guanjie_catalog.accuweather.forecast_hourly_imperial
# MAGIC TBLPROPERTIES (
# MAGIC   'delta.enableDeletionVectors' = 'false',
# MAGIC   'delta.enableIcebergCompatV2' = 'true',
# MAGIC   'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC   'delta.columnMapping.mode' = 'name'
# MAGIC ) AS
# MAGIC SELECT * FROM samples.accuweather.forecast_hourly_imperial;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE guanjie_catalog.accuweather.forecast_hourly_metric
# MAGIC TBLPROPERTIES (
# MAGIC   'delta.enableDeletionVectors' = 'false',
# MAGIC   'delta.enableIcebergCompatV2' = 'true',
# MAGIC   'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC   'delta.columnMapping.mode' = 'name'
# MAGIC ) AS
# MAGIC SELECT * FROM samples.accuweather.forecast_hourly_metric;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE guanjie_catalog.accuweather.historical_daily_calendar_imperial
# MAGIC TBLPROPERTIES (
# MAGIC   'delta.enableDeletionVectors' = 'false',
# MAGIC   'delta.enableIcebergCompatV2' = 'true',
# MAGIC   'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC   'delta.columnMapping.mode' = 'name'
# MAGIC ) AS
# MAGIC SELECT * FROM samples.accuweather.historical_daily_calendar_imperial;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE guanjie_catalog.accuweather.historical_daily_calendar_metric
# MAGIC TBLPROPERTIES (
# MAGIC   'delta.enableDeletionVectors' = 'false',
# MAGIC   'delta.enableIcebergCompatV2' = 'true',
# MAGIC   'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC   'delta.columnMapping.mode' = 'name'
# MAGIC ) AS
# MAGIC SELECT * FROM samples.accuweather.historical_daily_calendar_metric;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE guanjie_catalog.accuweather.historical_daynight_imperial
# MAGIC TBLPROPERTIES (
# MAGIC   'delta.enableDeletionVectors' = 'false',
# MAGIC   'delta.enableIcebergCompatV2' = 'true',
# MAGIC   'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC   'delta.columnMapping.mode' = 'name'
# MAGIC ) AS
# MAGIC SELECT * FROM samples.accuweather.historical_daynight_imperial;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE guanjie_catalog.accuweather.historical_daynight_metric
# MAGIC TBLPROPERTIES (
# MAGIC   'delta.enableDeletionVectors' = 'false',
# MAGIC   'delta.enableIcebergCompatV2' = 'true',
# MAGIC   'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC   'delta.columnMapping.mode' = 'name'
# MAGIC ) AS
# MAGIC SELECT * FROM samples.accuweather.historical_daynight_metric;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE guanjie_catalog.accuweather.historical_hourly_imperial
# MAGIC TBLPROPERTIES (
# MAGIC   'delta.enableDeletionVectors' = 'false',
# MAGIC   'delta.enableIcebergCompatV2' = 'true',
# MAGIC   'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC   'delta.columnMapping.mode' = 'name'
# MAGIC ) AS
# MAGIC SELECT * FROM samples.accuweather.historical_hourly_imperial;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE guanjie_catalog.accuweather.historical_hourly_metric
# MAGIC TBLPROPERTIES (
# MAGIC   'delta.enableDeletionVectors' = 'false',
# MAGIC   'delta.enableIcebergCompatV2' = 'true',
# MAGIC   'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC   'delta.columnMapping.mode' = 'name'
# MAGIC ) AS
# MAGIC SELECT * FROM samples.accuweather.historical_hourly_metric;
