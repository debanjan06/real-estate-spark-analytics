# 🏠 Distributed Big Data Analytics Framework for Real Estate Market Prediction

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Apache Spark](https://img.shields.io/badge/Apache%20Spark-3.5.5-orange.svg)](https://spark.apache.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)

A comprehensive machine learning framework for analyzing and predicting real estate market trends using Apache Spark's distributed computing capabilities. This project processes 100,000+ property records across major US metropolitan areas to identify key factors influencing property prices and market dynamics.

## 🚀 Key Features

- **Distributed Processing**: Leverages Apache Spark for scalable analysis of large real estate datasets
- **Advanced ML Models**: Implements Linear Regression, Random Forest, and Gradient Boosted Trees
- **Comprehensive Analytics**: Market trends, geographic analysis, temporal patterns, and feature importance
- **Interactive Visualizations**: Professional charts and dashboards using matplotlib and seaborn
- **Performance Optimization**: Memory management, caching strategies, and query optimization

## 📊 Key Findings

- **Physical attributes** (especially square footage) account for **80.3%** of price prediction importance
- **Geographic disparities**: San Francisco properties average **$4.73M** vs Houston's **$371K** (12x difference)
- **Property type hierarchy**: Multi-family homes lead with **$1.04M** average value
- **Model performance**: Linear Regression achieved highest R² of **0.144**

## 🏗️ Architecture

```
Real Estate Analytics Framework
├── Data Ingestion (Spark SQL)
├── ETL Pipeline (Data Cleaning & Transformation)
├── Feature Engineering (Spark ML Pipeline)
├── Distributed Model Training (MLlib)
├── Geospatial Analysis (Distance calculations)
└── Visualization & Reporting
```

## 📁 Project Structure

```
real-estate-spark-analytics/
│
├── data/
│   ├── raw/                    # Raw property data
│   ├── processed/              # Cleaned and transformed data
│   └── sample/                 # Sample datasets for testing
│
├── notebooks/
│   ├── Apache_Spark-Notebook.ipynb    # Main analysis notebook
│   ├── data_exploration.ipynb          # Initial data exploration
│   └── model_comparison.ipynb          # Model evaluation
│
├── src/
│   ├── __init__.py
│   ├── data_processing/
│   │   ├── __init__.py
│   │   ├── etl_pipeline.py
│   │   └── feature_engineering.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── regression_models.py
│   │   └── model_evaluation.py
│   ├── visualization/
│   │   ├── __init__.py
│   │   └── plots.py
│   └── utils/
│       ├── __init__.py
│       ├── spark_config.py
│       └── helpers.py
│
├── results/
│   ├── visualizations/         # Generated charts and plots
│   ├── models/                 # Trained model artifacts
│   ├── analysis_reports/       # Analysis summaries
│   └── csv_exports/            # Data exports
│
├── docs/
│   ├── research_paper.pdf      # Academic paper
│   ├── methodology.md          # Detailed methodology
│   └── api_documentation.md    # Code documentation
│
├── config/
│   ├── spark_config.yaml       # Spark configuration
│   └── model_params.yaml       # Model hyperparameters
│
├── requirements.txt            # Python dependencies
├── environment.yml             # Conda environment file
├── setup.py                    # Package setup
├── README.md                   # This file
├── LICENSE                     # MIT License
└── .gitignore                  # Git ignore rules
```

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.9+
- Java 8 or 11 (for Spark)
- Apache Spark 3.5.5
- Minimum 8GB RAM recommended

### Option 1: Conda Environment (Recommended)

```bash
# Clone the repository
git clone https://github.com/debanjan06/real-estate-spark-analytics.git
cd real-estate-spark-analytics

# Create conda environment
conda env create -f environment.yml
conda activate real-estate-analytics

# Install additional dependencies
pip install -r requirements.txt
```

### Option 2: Virtual Environment

```bash
# Clone the repository
git clone https://github.com/debanjan06/real-estate-spark-analytics.git
cd real-estate-spark-analytics

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Spark Setup

```bash
# Download and setup Spark (if not already installed)
wget https://archive.apache.org/dist/spark/spark-3.5.5/spark-3.5.5-bin-hadoop3.tgz
tar -xzf spark-3.5.5-bin-hadoop3.tgz
export SPARK_HOME=/path/to/spark-3.5.5-bin-hadoop3
export PATH=$SPARK_HOME/bin:$PATH
```

## 🚀 Quick Start

### 1. Run the Complete Analysis

```bash
# Start Jupyter notebook
jupyter notebook notebooks/Apache_Spark-Notebook.ipynb
```

### 2. Command Line Execution

```python
from src.data_processing.etl_pipeline import RealEstateETL
from src.models.regression_models import PropertyPricePredictor

# Initialize components
etl = RealEstateETL()
predictor = PropertyPricePredictor()

# Run analysis
etl.process_data()
results = predictor.train_models()
predictor.generate_report()
```

### 3. Generate Sample Data

```python
from src.utils.data_generator import generate_property_data

# Generate sample dataset
data = generate_property_data(n_properties=10000)
```

## 📈 Usage Examples

### Basic Price Prediction

```python
from src.models.regression_models import PropertyPricePredictor

predictor = PropertyPricePredictor()
predictor.load_model('linear_regression')

# Predict single property
prediction = predictor.predict({
    'sqft': 2500,
    'bedrooms': 3,
    'bathrooms': 2.5,
    'city': 'San Francisco',
    'property_type': 'single_family'
})

print(f"Predicted Price: ${prediction:,.2f}")
```

### Market Analysis

```python
from src.visualization.plots import MarketAnalyzer

analyzer = MarketAnalyzer()
analyzer.city_price_comparison()
analyzer.temporal_trends()
analyzer.feature_importance_plot()
```

### Custom Spark Configuration

```python
from src.utils.spark_config import get_spark_session

spark = get_spark_session(
    app_name="RealEstateAnalysis",
    driver_memory="8g",
    executor_memory="8g"
)
```

## 📊 Model Performance

| Model | RMSE | MAE | R² |
|-------|------|-----|-----|
| Linear Regression | $809,224 | $472,008 | **0.144** |
| Random Forest | $823,913 | $481,738 | 0.113 |
| Gradient Boosted Trees | $812,142 | $473,834 | 0.138 |

## 🎯 Feature Importance

1. **Physical Features (82.8%)**
   - Square footage: 80.3%
   - Property type: 2.5%

2. **Location Features (13.9%)**
   - City indicators: 10.7%
   - Distance to center: 3.2%

3. **Quality Features (2.8%)**
   - Neighborhood score: 1.8%
   - Crime/walkability scores: 1.0%

## 📈 Results & Visualizations

The analysis generates comprehensive visualizations including:

- **Geographic Price Distribution**: City-wise average prices
- **Property Type Analysis**: Price variations by property type
- **Model Performance Comparison**: RMSE, MAE, and R² metrics
- **Feature Importance Charts**: Random Forest feature rankings
- **Temporal Analysis**: Price trends over time
- **Correlation Matrix**: Feature relationship heatmap

All visualizations are saved in the `results/visualizations/` directory.

## 🔧 Configuration

### Spark Configuration (`config/spark_config.yaml`)

```yaml
driver:
  memory: "8g"
  memoryOverhead: "2g"
  maxResultSize: "2g"

executor:
  memory: "8g"
  cores: 4

sql:
  shuffle:
    partitions: 10

network:
  timeout: "1200s"
```

## 🧪 Testing

```bash
# Run unit tests
python -m pytest tests/

# Run specific test module
python -m pytest tests/test_models.py

# Generate coverage report
pytest --cov=src tests/
```

## 📚 Documentation

- **Methodology**: [docs/methodology.md](docs/methodology.md)
- **API Documentation**: [docs/api_documentation.md](docs/api_documentation.md)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add unit tests for new features
- Update documentation for API changes
- Ensure all tests pass before submitting PR

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Debanjan Shil**
- GitHub: [@debanjan06](https://github.com/debanjan06)
- Email: bl.sc.p2dsc24032@bl.students.amrita.edu
- Institution: Amrita Vishwa Vidyapeetham, Bengaluru
- Program: M.Tech in Data Science

## 🙏 Acknowledgments

- Dr. Manju Venugopalan (Supervisor)
- Apache Spark Community
- Amrita School of Computing
- Real Estate Data Providers

## 📊 Performance Metrics

- **Dataset Size**: 100,000 properties
- **Processing Time**: ~550 seconds
- **Cities Analyzed**: 6 major metropolitan areas
- **Feature Categories**: 4 (Physical, Location, Quality, Type)
- **Model Accuracy**: R² up to 0.144

## 🔮 Future Enhancements

- [ ] Deep Learning models (CNN, RNN)
- [ ] Real-time data streaming with Spark Streaming
- [ ] Enhanced geospatial analysis with PostGIS
- [ ] Web dashboard with Flask/Django
- [ ] Docker containerization
- [ ] Cloud deployment (AWS, Azure, GCP)
- [ ] API endpoints for model serving

## 📞 Support

For questions or support, please:
1. Check the [documentation](docs/)
2. Search existing [issues](https://github.com/debanjan06/real-estate-spark-analytics/issues)
3. Create a new issue if needed
4. Contact the author via email

---

**⭐ Star this repository if you find it helpful!**
