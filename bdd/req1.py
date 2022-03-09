from functools import reduce
from typing import List, Tuple

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.functions import col, lit, when


def get_total_number_of_clients(client_details_path):
    
    spark = SparkSession.builder().getOrCreate()
    df = spark.read.csv(client_details_path)

    return df.select("id").distinct().count()



