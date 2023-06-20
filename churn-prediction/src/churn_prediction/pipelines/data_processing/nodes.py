"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.10
"""
import pandas as pd
import numpy as np

def preprocess_abandono(abandono: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses the data for companies.

    Args:
        companies: Raw data.
    Returns:
        Preprocessed data, with `company_rating` converted to a float and
        `iata_approved` converted to boolean.
        """

    # When the division is 0, resulting variable will be zero:
    # EstimatedSalary / CreditScore
    abandono['EstimatedSalary_CreditScore_Ratio'] = np.where(abandono['CreditScore'] == 0, 0, abandono['EstimatedSalary'] / abandono['CreditScore'])

    # CreditScore / EstimatedSalary
    abandono['CreditScore_EstimatedSalary_Ratio'] = np.where(abandono['EstimatedSalary'] == 0, 0, abandono['CreditScore'] / abandono['EstimatedSalary'])

    # Balance / EstimatedSalary
    abandono['Balance_EstimatedSalary_Ratio'] = np.where(abandono['EstimatedSalary'] == 0, 0, abandono['Balance'] / abandono['EstimatedSalary'])

    # Balance is zero
    abandono['Balance_IsZero'] = abandono['Balance'] == 0

    # Balance / Geography Mean Balance
    mean_balance_germany = 120000  # from EDA
    mean_balance_spain_france = 60000 

    abandono['Balance_GeographyMean_Ratio'] = abandono['Balance'] / np.where(abandono['Geography'] == 'Germany', mean_balance_germany, mean_balance_spain_france)

    # Tenure / Age
    abandono['Tenure_Age_Ratio'] = np.where(abandono['Age'] == 0, 0, abandono['Tenure'] / abandono['Age'])

    # NumOf / Age
    abandono['NumOfProducts_Tenure_Ratio'] = np.where(abandono['Tenure'] == 0, 0, abandono['NumOfProducts'] / abandono['Tenure'])


    #########
    # From the first feature engineering loop:
    #########

    # Drop irrelevant variables
    abandono = abandono.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)

    # Binning 
    #-- CreditScore column
    bins = [350, 500, 650, 800, 850]  # Define the bin edges
    labels = ['Low', 'Medium', 'High', 'Very High']  # Define the bin labels

    abandono['CreditScoreBins'] = pd.cut(abandono['CreditScore'], bins=bins, labels=labels)

    # One hot encoding for categorical variables
    abandono = pd.get_dummies(abandono, columns=['Geography', 'Gender', 'CreditScoreBins', 'NumOfProducts'], drop_first=True)
    #########

    return abandono