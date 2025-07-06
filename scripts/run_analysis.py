#!/usr/bin/env python3
"""
Script to run the complete real estate analysis
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from data_processing.etl_pipeline import RealEstateETL
from models.regression_models import PropertyPricePredictor
from visualization.plots import MarketAnalyzer

def main():
    print("Starting Real Estate Analysis...")
    
    # Initialize components
    etl = RealEstateETL()
    predictor = PropertyPricePredictor(etl.spark)
    analyzer = MarketAnalyzer()
    
    # Run analysis
    print("Processing data...")
    # Add your analysis steps here
    
    print("Analysis complete!")

if __name__ == "__main__":
    main()