"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.10
"""
import pandas as pd

def preprocess_abandono(abandono: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses the data for companies.

    Args:
        companies: Raw data.
    Returns:
        Preprocessed data, with `company_rating` converted to a float and
        `iata_approved` converted to boolean.
    """

    # Drop irrelevant info
    abandono = abandono.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)

    # Normalize Age column
    abandono['AgeNormalized'] = (abandono['Age'] - abandono['Age'].min()) / (abandono['Age'].max() - abandono['Age'].min())

    # Normalize EstimatedSalary column
    abandono['EstimatedSalaryNormalized'] = (abandono['EstimatedSalary'] - abandono['EstimatedSalary'].min()) / (abandono['EstimatedSalary'].max() - abandono['EstimatedSalary'].min())

    # Drop the original Age and EstimatedSalary columns
    abandono = abandono.drop(['Age', 'EstimatedSalary'], axis=1)

    ## Binning ## 
    # CreditScore column
    bins = [350, 500, 650, 800, 850]  # Define the bin edges
    labels = ['Low', 'Medium', 'High', 'Very High']  # Define the bin labels

    abandono['CreditScoreBins'] = pd.cut(abandono['CreditScore'], bins=bins, labels=labels)

    # Balance 
    bin_edges = [0, 50000, 100000, 150000, 200000, 250000]
    bin_labels = ['0-50k', '50k-100k', '100k-150k', '150k-200k', '200k-250k']

    abandono['Balance_Bins'] = pd.cut(abandono['Balance'], bins=bin_edges, labels=bin_labels)

    # Create a boolean column for when Balance is zero
    abandono['Balance_IsZero'] = abandono['Balance'] == 0

    abandono = abandono.drop(['Balance', 'CreditScore'], axis=1)

    ### One hot encoding for categorical variables
    abandono = pd.get_dummies(abandono, columns=['Geography', 'Gender', 'CreditScoreBins', 'Balance_Bins'], drop_first=True)
    
    return abandono