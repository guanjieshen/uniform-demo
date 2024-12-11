# Databricks notebook source
# MAGIC %sql use catalog guanjie_catalog

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE gold.sales_revenue_by_customer
# MAGIC   TBLPROPERTIES (
# MAGIC     'delta.enableDeletionVectors' = 'false',
# MAGIC     'delta.enableIcebergCompatV2' = 'true',
# MAGIC     'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC     'delta.columnMapping.mode' = 'name'
# MAGIC   ) AS
# MAGIC SELECT
# MAGIC     o_custkey,
# MAGIC     YEAR(o_orderdate) AS year,
# MAGIC     SUM(l_extendedprice * (1 -l_discount)) AS total_revenue
# MAGIC FROM silver.orders AS o
# MAGIC JOIN silver.lineitem AS l
# MAGIC   ON o.o_orderkey = l.l_orderkey
# MAGIC GROUP BY o_custkey, YEAR(o_orderdate);

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE
# MAGIC OR REPLACE TABLE gold.top_shipping_modes
# MAGIC TBLPROPERTIES (
# MAGIC   'delta.enableDeletionVectors' = 'false',
# MAGIC   'delta.enableIcebergCompatV2' = 'true',
# MAGIC   'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC   'delta.columnMapping.mode' = 'name'
# MAGIC ) AS
# MAGIC SELECT
# MAGIC   l_shipmode,
# MAGIC   SUM(l_extendedprice * (1 - l_discount)) AS total_revenue
# MAGIC FROM
# MAGIC   silver.lineitem
# MAGIC GROUP BY
# MAGIC   l_shipmode
# MAGIC ORDER BY
# MAGIC   total_revenue DESC;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE
# MAGIC OR REPLACE TABLE gold.order_fulfillment_time
# MAGIC TBLPROPERTIES (
# MAGIC   'delta.enableDeletionVectors' = 'false',
# MAGIC   'delta.enableIcebergCompatV2' = 'true',
# MAGIC   'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC   'delta.columnMapping.mode' = 'name'
# MAGIC ) AS
# MAGIC SELECT
# MAGIC   l_orderkey,
# MAGIC   o_custkey,
# MAGIC   DATEDIFF(l_receiptdate, o_orderdate) AS days_to_fulfill,
# MAGIC   CASE
# MAGIC     WHEN DATEDIFF(l_receiptdate, o_orderdate) <= 7 THEN 'Fast'
# MAGIC     WHEN DATEDIFF(l_receiptdate, o_orderdate) <= 14 THEN 'Medium'
# MAGIC     ELSE 'Slow'
# MAGIC   END AS fulfillment_category
# MAGIC FROM
# MAGIC   silver.orders AS o
# MAGIC   JOIN silver.lineitem AS l ON o.o_orderkey = l.l_orderkey
# MAGIC WHERE
# MAGIC   l_receiptdate IS NOT NULL
# MAGIC   AND o_orderdate IS NOT NULL;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE gold.customer_profitability
# MAGIC TBLPROPERTIES (
# MAGIC   'delta.enableDeletionVectors' = 'false',
# MAGIC   'delta.enableIcebergCompatV2' = 'true',
# MAGIC   'delta.universalFormat.enabledFormats' = 'iceberg',
# MAGIC   'delta.columnMapping.mode' = 'name'
# MAGIC ) AS
# MAGIC SELECT
# MAGIC   c.c_custkey,
# MAGIC   c.c_name AS customer_name,
# MAGIC   SUM(
# MAGIC     (l.l_extendedprice * (1 - l.l_discount)) - (l.l_quantity * 5)
# MAGIC   ) AS net_profit
# MAGIC FROM
# MAGIC   silver.customer AS c
# MAGIC   JOIN silver.orders AS o ON c.c_custkey = o.o_custkey
# MAGIC   JOIN silver.lineitem AS l ON o.o_orderkey = l.l_orderkey
# MAGIC GROUP BY
# MAGIC   c.c_custkey,
# MAGIC   c.c_name
# MAGIC ORDER BY
# MAGIC   net_profit DESC;
