"""
Visualization utilities for real estate analysis
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

class MarketAnalyzer:
    def __init__(self, style='seaborn-v0_8-darkgrid'):
        plt.style.use(style)
        
    def city_price_comparison(self, city_data, save_path=None):
        """Create city price comparison chart"""
        fig, ax = plt.subplots(figsize=(15, 8))
        bars = ax.bar(city_data['city'], city_data['avg_price'], color='skyblue')
        ax.set_title('Average Property Price by City', fontsize=16)
        ax.set_xlabel('City', fontsize=14)
        ax.set_ylabel('Average Price ($)', fontsize=14)
        ax.set_xticklabels(city_data['city'], rotation=45)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                    f'${height:,.0f}', ha='center', va='bottom')
        
        plt.tight_layout()
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
    
    def feature_importance_plot(self, feature_importance_df, top_n=15, save_path=None):
        """Create feature importance visualization"""
        fig, ax = plt.subplots(figsize=(12, 10))
        top_features = feature_importance_df.head(top_n)
        y_pos = np.arange(len(top_features))
        
        bars = ax.barh(y_pos, top_features['importance'][::-1], color='skyblue')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(top_features['feature'][::-1])
        ax.set_xlabel('Importance', fontsize=14)
        ax.set_title(f'Top {top_n} Feature Importances', fontsize=16)
        ax.grid(True, alpha=0.3, axis='x')
        
        # Add value labels
        for i, bar in enumerate(bars):
            width = bar.get_width()
            ax.text(width + 0.001, bar.get_y() + bar.get_height()/2, 
                    f'{width:.3f}', ha='left', va='center', fontsize=10)
        
        plt.tight_layout()
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
    
    def model_performance_comparison(self, model_results, save_path=None):
        """Compare model performance metrics"""
        fig, ax = plt.subplots(figsize=(12, 8))
        models = list(model_results.keys())
        x = np.arange(len(models))
        width = 0.25
        
        rmse_values = [model_results[m]['rmse']/1000 for m in models]
        mae_values = [model_results[m]['mae']/1000 for m in models]
        r2_values = [model_results[m]['r2']*100 for m in models]
        
        bars1 = ax.bar(x - width, rmse_values, width, label='RMSE (in $1000s)')
        bars2 = ax.bar(x, mae_values, width, label='MAE (in $1000s)')
        bars3 = ax.bar(x + width, r2_values, width, label='R² (x100)')
        
        ax.set_ylabel('Metric Value', fontsize=14)
        ax.set_title('Model Performance Comparison', fontsize=16)
        ax.set_xticks(x)
        ax.set_xticklabels(models)
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()