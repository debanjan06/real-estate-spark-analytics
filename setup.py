"""
Setup script for Real Estate Analytics Framework
"""

from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read requirements from requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="real-estate-analytics",
    version="1.0.0",
    author="Debanjan Shil",
    author_email="bl.sc.p2dsc24032@bl.students.amrita.edu",
    description="Distributed Big Data Analytics Framework for Real Estate Market Prediction Using Apache Spark",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/debanjan06/real-estate-spark-analytics",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Office/Business :: Financial :: Investment",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "isort>=5.0.0",
        ],
        "docs": [
            "sphinx>=7.0.0",
            "sphinx-rtd-theme>=1.3.0",
        ],
        "viz": [
            "plotly>=5.15.0",
            "dash>=2.10.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "real-estate-analytics=real_estate_analytics.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "real_estate_analytics": [
            "config/*.yaml",
            "data/sample/*.csv",
        ],
    },
    keywords=[
        "real estate",
        "machine learning",
        "apache spark",
        "data analytics",
        "property prediction",
        "big data",
        "distributed computing",
        "price prediction",
    ],
    project_urls={
        "Bug Reports": "https://github.com/debanjan06/real-estate-spark-analytics/issues",
        "Source": "https://github.com/debanjan06/real-estate-spark-analytics",
        "Documentation": "https://github.com/debanjan06/real-estate-spark-analytics/docs",
    },
)