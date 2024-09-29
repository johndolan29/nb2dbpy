# Databricks notebook source
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# COMMAND ----------

df = pd.read_csv("data.csv")
df = df.dropna()

# COMMAND ----------

df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month

# COMMAND ----------

# MAGIC %run ./utils.py
