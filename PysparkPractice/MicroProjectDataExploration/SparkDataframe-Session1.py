from pyspark.sql import *
import json
import os
from pyspark import SparkFiles

with open('PysparkPractice/MicroProjectDataExploration/pathList.json','r') as file:
    pathlist = json.load(file)

datasetPath = pathlist['paths']['url']['sfgov']
print(datasetPath)

sc.addFile(datasetPath)

spark = SparkSession.builder.appName("csv_load").getOrCreate()
df = spark.read.csv(datasetPath,inferSchema =True,header = True)
df.show()

