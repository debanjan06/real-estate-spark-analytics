"""
Spark configuration utilities
"""
import os
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf

def get_spark_session(app_name="RealEstateAnalysis", **kwargs):
    """Create and configure Spark session with optimized settings"""
    
    # Set environment variables
    os.environ['PYSPARK_PYTHON'] = sys.executable
    os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
    os.environ['SPARK_LOCAL_IP'] = '127.0.0.1'
    
    # Default configuration
    default_config = {
        "spark.driver.memory": "8g",
        "spark.executor.memory": "8g",
        "spark.driver.memoryOverhead": "2g",
        "spark.executor.cores": "4",
        "spark.sql.shuffle.partitions": "10",
        "spark.network.timeout": "1200s",
        "spark.executor.heartbeatInterval": "120s",
        "spark.serializer": "org.apache.spark.serializer.KryoSerializer",
        "spark.driver.maxResultSize": "2g",
        "spark.sql.execution.arrow.pyspark.enabled": "false"
    }
    
    # Update with user-provided config
    config = {**default_config, **kwargs}
    
    # Create Spark configuration
    conf = SparkConf()
    for key, value in config.items():
        conf.set(key, value)
    
    # Create Spark session
    spark = SparkSession.builder \
        .appName(app_name) \
        .config(conf=conf) \
        .master("local[4]") \
        .getOrCreate()
    
    return spark