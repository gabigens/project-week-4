# Bank Marketing Campaign Analysis

## Project Overview
This project analyzes a Portuguese bank's marketing campaign dataset to predict whether clients will subscribe to a term deposit. The analysis includes comprehensive exploratory data analysis (EDA), data preprocessing, feature engineering, and machine learning model development.

## Dataset
The dataset contains information about bank marketing campaigns conducted via phone calls. It includes:
- **41,188 records** (plus 1 header row) with **21 features**
- Client demographic information (age, job, marital status, education)
- Campaign details (contact type, month, duration, number of contacts)
- Economic indicators (employment rate, consumer confidence, euribor rate)
- Target variable: whether the client subscribed to a term deposit (yes/no)

### Features Description:
- **age**: Client's age
- **job**: Type of job
- **marital**: Marital status
- **education**: Education level
- **default**: Has credit in default?
- **housing**: Has housing loan?
- **loan**: Has personal loan?
- **contact**: Contact communication type
- **month**: Last contact month
- **day_of_week**: Last contact day of the week
- **duration**: Last contact duration (seconds)
- **campaign**: Number of contacts performed during this campaign
- **pdays**: Days since last contact from previous campaign
- **previous**: Number of contacts before this campaign
- **poutcome**: Outcome of previous marketing campaign
- **emp_var_rate**: Employment variation rate
- **cons_price_idx**: Consumer price index
- **cons_conf_idx**: Consumer confidence index
- **euribor3m**: Euribor 3 month rate
- **nr_employed**: Number of employees
- **y**: Target - Has the client subscribed? (0=no, 1=yes)

## Project Structure
```
project-week-4/
├── data/
│   └── bank.csv                          # Bank marketing dataset
├── notebooks/
│   └── bank_marketing_analysis.ipynb     # Main analysis notebook
├── src/                                   # Source code and utilities
│   ├── __init__.py                       # Package initialization
│   └── data_loader.py                    # Data loading utilities
├── examples/                              # Example scripts
│   └── quick_start.py                    # Quick start example
├── requirements.txt                       # Python dependencies
├── .gitignore                            # Git ignore file
├── CONTRIBUTING.md                       # Contribution guidelines
└── README.md                             # Project documentation
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup
1. Clone the repository:
```bash
git clone https://github.com/gabigens/project-week-4.git
cd project-week-4
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Analysis
1. Navigate to the notebooks directory:
```bash
cd notebooks
```

2. Start Jupyter Notebook:
```bash
jupyter notebook
```

3. Open `bank_marketing_analysis.ipynb` and run all cells

### Analysis Steps
The notebook includes the following sections:
1. **Data Loading and Inspection**: Load dataset and examine basic statistics
2. **Exploratory Data Analysis**: Visualize distributions and relationships
3. **Data Preprocessing**: Handle categorical variables and scale features
4. **Model Building**: Train multiple classification models
5. **Model Evaluation**: Compare performance metrics
6. **Feature Importance**: Identify key predictive features
7. **Insights and Recommendations**: Business insights and next steps

## Models Used
The project implements and compares four machine learning models:
- **Logistic Regression**: Baseline linear model
- **Decision Tree**: Non-linear tree-based model
- **Random Forest**: Ensemble of decision trees
- **Gradient Boosting**: Advanced boosting algorithm

## Key Results
- All models achieve **ROC-AUC scores above 0.85**
- **Call duration** is the most important predictor
- **Previous campaign outcome** strongly influences subscription likelihood
- Economic indicators significantly affect customer behavior
- The models can effectively prioritize customer contacts for marketing campaigns

## Business Insights
1. **Target High-Value Segments**: Focus on customers with positive previous campaign outcomes
2. **Optimize Call Quality**: Longer, more engaging calls lead to better conversion
3. **Time Campaigns Strategically**: Consider economic indicators and seasonal factors
4. **Personalize Approach**: Different demographic segments respond differently
5. **Use Predictive Scoring**: Implement model to prioritize customer contacts

## Future Improvements
- Address class imbalance with advanced techniques (SMOTE, class weights)
- Implement hyperparameter tuning for optimal model performance
- Develop customer segmentation analysis
- Create deployment-ready prediction API
- Build interactive dashboard for campaign monitoring
- Conduct A/B testing with model predictions

## Technologies Used
- **Python 3.x**: Programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Matplotlib & Seaborn**: Data visualization
- **Scikit-learn**: Machine learning algorithms and evaluation
- **Jupyter Notebook**: Interactive development environment

## Contributing
This is a mini project for educational purposes. Feel free to fork and extend!

## License
This project is open source and available for educational use.

## Presentation
Project presentation: [View on Canva](https://www.canva.com/design/DAG3WAV_K10/ixtm2GZKIN1-BBEeELXa1g/edit)

## Acknowledgments
- Dataset source: UCI Machine Learning Repository
- Inspired by real-world bank marketing campaigns
- Built as part of a data science mini project
