# API Documentation

## RealEstateETL Class

### Methods

#### `generate_sample_data(n_properties=100000)`
Generates sample real estate data for analysis.

**Parameters:**
- `n_properties` (int): Number of properties to generate

**Returns:**
- List of property records

## PropertyPricePredictor Class

### Methods

#### `train_linear_regression(train_df)`
Trains a linear regression model on the provided dataset.

**Parameters:**
- `train_df`: Spark DataFrame with training data

**Returns:**
- Trained pipeline model