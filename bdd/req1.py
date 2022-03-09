from functools import reduce
from typing import List, Tuple

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.functions import col, lit, when

dir_path = os.path.dirname(os.path.abspath(__file__))

spark = SparkSession.builder.master("local").appName("CreateReq1").getOrCreate()

def get_total_number_of_clients(client_details_path):
    
    spark = SparkSession.builder().getOrCreate()
    df = spark.read.option("header", True).option("inferSchema", True).csv(
        dir_path + "/../fixtures/client_details.csv")

    return df.select("id").distinct().count()



