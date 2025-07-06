"""
Unit tests for machine learning models
"""
import pytest
from pyspark.sql import SparkSession
from src.models.regression_models import PropertyPricePredictor

@pytest.fixture(scope="session")
def spark_session():
    return SparkSession.builder \
        .appName("TestSession") \
        .master("local[2]") \
        .getOrCreate()

def test_property_price_predictor_init(spark_session):
    predictor = PropertyPricePredictor(spark_session)
    assert predictor.spark is not None
    assert len(predictor.models) == 0

def test_feature_preparation(spark_session):
    predictor = PropertyPricePredictor(spark_session)
    # Add test for feature preparation
    pass