"""
Quick Start Example for Bank Marketing Analysis

This script demonstrates basic usage of the data loader
and provides a simple analysis workflow.
"""

import sys
from pathlib import Path

# Add parent directory to path to import src modules
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from src.data_loader import BankMarketingDataLoader
    import pandas as pd
    import numpy as np
    
    # Initialize data loader
    print("=" * 70)
    print("Bank Marketing Analysis - Quick Start")
    print("=" * 70)
    
    loader = BankMarketingDataLoader('../data/bank.csv')
    df = loader.load_data()
    
    print("\n✓ Dataset loaded successfully!")
    
    # Get summary
    summary = loader.get_summary()
    print(f"\nDataset contains {summary['shape'][0]:,} records and {summary['shape'][1]} features")
    
    # Show target distribution
    print("\nTarget Variable Distribution:")
    target_counts = df['y'].value_counts()
    for value, count in target_counts.items():
        pct = (count / len(df)) * 100
        print(f"  {value}: {count:,} ({pct:.1f}%)")
    
    # Show sample data
    print("\nSample Records:")
    print(df.head(3).to_string())
    
    # Basic statistics
    print("\nAge Statistics:")
    print(f"  Mean: {df['age'].mean():.1f} years")
    print(f"  Median: {df['age'].median():.1f} years")
    print(f"  Range: {df['age'].min():.0f} - {df['age'].max():.0f} years")
    
    print("\nCall Duration Statistics:")
    print(f"  Mean: {df['duration'].mean():.0f} seconds")
    print(f"  Median: {df['duration'].median():.0f} seconds")
    
    print("\nTop 5 Most Common Jobs:")
    print(df['job'].value_counts().head(5).to_string())
    
    print("\n" + "=" * 70)
    print("For complete analysis, open notebooks/bank_marketing_analysis.ipynb")
    print("=" * 70)
    
except ImportError as e:
    print(f"Error: Required packages not installed - {e}")
    print("\nPlease install required packages:")
    print("  pip install -r requirements.txt")
except FileNotFoundError as e:
    print(f"Error: {e}")
    print("\nMake sure you're running this script from the examples/ directory")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
