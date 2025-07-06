# Analysis Results

This directory contains the comprehensive analysis results from the Real Estate Analytics Framework.

## 📊 CSV Analysis Files

### Market Analysis
- **`city_analysis.csv`** - Average prices and metrics by city
- **`property_type_analysis.csv`** - Analysis by property type (single-family, condo, etc.)
- **`price_segment_analysis.csv`** - Price segmentation (Budget, Mid-range, High-end, Luxury)
- **`neighborhood_analysis.csv`** - Impact of neighborhood scores on pricing

### Temporal & Geographic Analysis
- **`temporal_analysis.csv`** - Price trends over time (25 time periods)
- **`market_velocity_analysis.csv`** - Days on market by city and property type
- **`price_appreciation_analysis.csv`** - Price trends by property age

### Machine Learning Results
- **`model_comparison.csv`** - Performance metrics for all ML models
- **`feature_importance.csv`** - Random Forest feature importance rankings
- **`model_predictions_sample.csv`** - Sample predictions with error analysis
- **`price_correlations.csv`** - Correlation analysis between features and price

### Sample Data
- **`property_sample.csv`** - 1% sample of the complete dataset (1,000 properties)

## 📈 Visualizations

### Market Overview
- **`analysis_dashboard.png`** - Comprehensive dashboard with multiple charts
- **`price_by_city.png`** - Average property prices across major cities
- **`price_by_type.png`** - Price comparison by property type
- **`price_distribution.png`** - Overall price distribution histogram

### Advanced Analytics
- **`feature_importance.png`** - Top 15 most important features for price prediction
- **`feature_importance_by_category.png`** - Feature importance grouped by category
- **`correlation_matrix.png`** - Feature correlation heatmap
- **`sqft_vs_price.png`** - Relationship between square footage and price

### Model Performance
- **`model_comparison.png`** - Visual comparison of ML model performance (RMSE, MAE, R²)

## 🎯 Key Insights

### Top Price Predictors
1. **Square Footage** (80.3% importance)
2. **City Location** (10.7% importance) 
3. **Distance to Center** (3.2% importance)

### Geographic Insights
- **San Francisco**: $4.73M average (premium market)
- **New York**: $1.65M average (high-value market)
- **Houston**: $371K average (affordable market)

### Model Performance
- **Linear Regression**: R² = 0.144 (best performing)
- **Random Forest**: R² = 0.113 
- **Gradient Boosted Trees**: R² = 0.138

### Market Dynamics
- **Average Days on Market**: 29.7 days
- **Property Types**: Multi-family homes command highest prices ($1.04M avg)
- **Neighborhood Impact**: 47.8% price premium in top-rated neighborhoods

## 📊 Dataset Statistics

- **Total Properties Analyzed**: 100,000
- **Cities Covered**: 6 major metropolitan areas
- **Time Period**: 25 months of market data
- **Features**: 18 property characteristics
- **Processing Time**: ~550 seconds

## 🔧 Technical Details

- **Framework**: Apache Spark 3.5.5
- **Language**: PySpark (Python)
- **ML Library**: Spark MLlib
- **Visualization**: Matplotlib, Seaborn
- **Data Processing**: Distributed computing with optimized configuration

## 📁 File Sizes

- **Total CSV Files**: ~218 KB (12 files)
- **Total Visualizations**: ~2.1 MB (9 PNG files)
- **Largest File**: `property_sample.csv` (192 KB)
- **Dashboard**: `analysis_dashboard.png` (615 KB)

## 🚀 Usage

These results can be used for:
- **Investment Decisions**: City and property type analysis
- **Market Research**: Temporal trends and geographic patterns
- **Model Validation**: Performance metrics and predictions
- **Academic Research**: Comprehensive real estate market analysis
- **Portfolio Demonstrations**: Professional data science capabilities

All visualizations are publication-ready with high DPI (300) for professional presentations.