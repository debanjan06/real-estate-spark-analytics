"""
Unit tests for ETL pipeline
"""
import pytest
from src.data_processing.etl_pipeline import RealEstateETL

def test_etl_initialization():
    etl = RealEstateETL()
    assert etl.spark is not None

def test_data_cleaning():
    # Add tests for data cleaning functionality
    pass