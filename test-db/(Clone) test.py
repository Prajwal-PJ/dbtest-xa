# Databricks notebook source
# MAGIC %sql
# MAGIC select * from imdb_movies_rating limit 10

# COMMAND ----------

# MAGIC %fs ls

# COMMAND ----------

# MAGIC %fs dbfs:/databricks-datasets/

# COMMAND ----------

# MAGIC %fs ls dbfs:/databricks-datasets/

# COMMAND ----------

df=spark.read.csv(imdb_movies_rating, header=True, inferSchema=True)

# COMMAND ----------

spark.sql('show tables').show()

# COMMAND ----------

# MAGIC %sql
# MAGIC describe detail imdb_movies_rating

# COMMAND ----------

# MAGIC %sql
# MAGIC describe history imdb_movies_rating

# COMMAND ----------

# MAGIC %fs ls s3://databricks-workspace-stack-27628-bucket/unity-catalog/4365251991476007/__unitystorage/catalogs/80363fbe-77c7-44a5-b47a-615a97fa4d23/tables/271bced3-8061-47a8-b1dd-b828b2d41858

# COMMAND ----------


