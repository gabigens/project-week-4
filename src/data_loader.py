"""
Data loader module for Bank Marketing dataset
"""

import pandas as pd
import numpy as np
from pathlib import Path


class BankMarketingDataLoader:
    """Class to load and provide basic info about the bank marketing dataset"""
    
    def __init__(self, data_path='../data/bank.csv'):
        """Initialize the data loader with the path to the dataset"""
        self.data_path = Path(data_path)
        self.df = None
        
    def load_data(self):
        """Load the dataset from CSV file"""
        if not self.data_path.exists():
            raise FileNotFoundError(f"Dataset not found at {self.data_path}")
        
        self.df = pd.read_csv(self.data_path)
        return self.df
    
    def get_summary(self):
        """Get summary statistics of the dataset"""
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        
        summary = {
            'shape': self.df.shape,
            'columns': self.df.columns.tolist(),
            'target_distribution': self.df['y'].value_counts().to_dict(),
            'missing_values': self.df.isnull().sum().sum(),
            'numeric_features': self.df.select_dtypes(include=[np.number]).columns.tolist(),
            'categorical_features': self.df.select_dtypes(include=['object']).columns.tolist()
        }
        return summary
    
    def get_feature_info(self):
        """Get information about each feature"""
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        
        feature_info = {}
        for col in self.df.columns:
            feature_info[col] = {
                'dtype': str(self.df[col].dtype),
                'unique_values': self.df[col].nunique(),
                'missing': self.df[col].isnull().sum()
            }
        return feature_info


if __name__ == "__main__":
    # Example usage
    loader = BankMarketingDataLoader()
    df = loader.load_data()
    
    print("=" * 60)
    print("Bank Marketing Dataset Summary")
    print("=" * 60)
    
    summary = loader.get_summary()
    print(f"\nDataset Shape: {summary['shape']}")
    print(f"Total Records: {summary['shape'][0]}")
    print(f"Total Features: {summary['shape'][1]}")
    print(f"Missing Values: {summary['missing_values']}")
    
    print(f"\nTarget Distribution:")
    for key, value in summary['target_distribution'].items():
        percentage = (value / summary['shape'][0]) * 100
        print(f"  {key}: {value} ({percentage:.2f}%)")
    
    print(f"\nNumeric Features ({len(summary['numeric_features'])}):")
    print(f"  {', '.join(summary['numeric_features'])}")
    
    print(f"\nCategorical Features ({len(summary['categorical_features'])}):")
    print(f"  {', '.join(summary['categorical_features'])}")
    
    print("\n" + "=" * 60)
    print("Feature Information")
    print("=" * 60)
    
    feature_info = loader.get_feature_info()
    for feature, info in feature_info.items():
        print(f"\n{feature}:")
        print(f"  Type: {info['dtype']}")
        print(f"  Unique Values: {info['unique_values']}")
        print(f"  Missing Values: {info['missing']}")
