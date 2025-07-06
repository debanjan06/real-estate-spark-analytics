"""
Machine Learning Models for Property Price Prediction
"""
from pyspark.ml.feature import VectorAssembler, StandardScaler, StringIndexer, OneHotEncoder
from pyspark.ml.regression import LinearRegression, GBTRegressor, RandomForestRegressor
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml import Pipeline
import pandas as pd

class PropertyPricePredictor:
    def __init__(self, spark_session=None):
        self.spark = spark_session
        self.models = {}
        self.pipelines = {}
        
    def prepare_features(self, df):
        """Prepare features for machine learning"""
        # Encode categorical variables
        property_type_indexer = StringIndexer(inputCol="property_type", outputCol="property_type_idx")
        property_type_encoder = OneHotEncoder(inputCol="property_type_idx", outputCol="property_type_vec")
        
        city_indexer = StringIndexer(inputCol="city", outputCol="city_idx")
        city_encoder = OneHotEncoder(inputCol="city_idx", outputCol="city_vec")
        
        # Feature columns
        feature_columns = [
            "bedrooms", "bathrooms", "sqft", "lot_size", "age", "garage_spaces",
            "school_rating", "crime_score", "walkability_score", "neighborhood_score",
            "distance_to_center", "property_type_vec", "city_vec"
        ]
        
        # Assemble features
        assembler = VectorAssembler(inputCols=feature_columns, outputCol="features")
        
        return [property_type_indexer, property_type_encoder, city_indexer, 
                city_encoder, assembler]
    
    def train_linear_regression(self, train_df):
        """Train Linear Regression model"""
        stages = self.prepare_features(train_df)
        stages.extend([
            StandardScaler(inputCol="features", outputCol="scaled_features"),
            LinearRegression(featuresCol="scaled_features", labelCol="price", 
                           predictionCol="predicted_price")
        ])
        
        pipeline = Pipeline(stages=stages)
        model = pipeline.fit(train_df)
        
        self.pipelines['linear_regression'] = pipeline
        self.models['linear_regression'] = model
        
        return model
    
    def train_random_forest(self, train_df):
        """Train Random Forest model"""
        stages = self.prepare_features(train_df)
        stages.append(
            RandomForestRegressor(featuresCol="features", labelCol="price", 
                                predictionCol="predicted_price", numTrees=100)
        )
        
        pipeline = Pipeline(stages=stages)
        model = pipeline.fit(train_df)
        
        self.pipelines['random_forest'] = pipeline
        self.models['random_forest'] = model
        
        return model
    
    def evaluate_model(self, model, test_df):
        """Evaluate model performance"""
        predictions = model.transform(test_df)
        
        evaluator_rmse = RegressionEvaluator(labelCol="price", predictionCol="predicted_price", metricName="rmse")
        evaluator_mae = RegressionEvaluator(labelCol="price", predictionCol="predicted_price", metricName="mae")
        evaluator_r2 = RegressionEvaluator(labelCol="price", predictionCol="predicted_price", metricName="r2")
        
        rmse = evaluator_rmse.evaluate(predictions)
        mae = evaluator_mae.evaluate(predictions)
        r2 = evaluator_r2.evaluate(predictions)
        
        return {
            'rmse': rmse,
            'mae': mae,
            'r2': r2,
            'predictions': predictions
        }