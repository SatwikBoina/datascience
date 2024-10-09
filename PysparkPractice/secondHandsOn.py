from pyspark.sql import *

if __name__=="__main__":
    spark  = SparkSession.builder.appName("Hello spark").master("local[2]").getOrCreate()
    datalist = [('Venkata Ramana Murthy',"Nanna"),("Sailaja","Amma"),('sai bharath','Tammudu')]
    df = spark.createDataFrame(datalist).toDF("Name","Relation")
    df.show()
