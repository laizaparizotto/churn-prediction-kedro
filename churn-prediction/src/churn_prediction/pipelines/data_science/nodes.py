"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.10
"""
import logging
from typing import Dict, Tuple

import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

def split_data(data: pd.DataFrame, parameters: Dict) -> Tuple:
    """Splits data into features and targets training and test sets.

    Args:
        data: Data containing features and target.
        parameters: Parameters defined in parameters/data_science.yml.
    Returns:
        Split data.
    """
    X = data.drop('Exited', axis=1)
    y = data["Exited"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=parameters["test_size"], random_state=parameters["random_state"]
    )

    # Perform standard scaling on the features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)

    return X_train, X_test, y_train, y_test


def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> RandomForestClassifier:
    """Trains the RandomForestClassifier.

    Args:
        X_train: Training data of independent features.
        y_train: Training data for price.

    Returns:
        Trained model.
    """
    classifier = RandomForestClassifier()
    classifier.fit(X_train, y_train)
    return classifier


def evaluate_model(
    classifier: RandomForestClassifier, X_test: pd.DataFrame, y_test: pd.Series
):
    """Calculates and logs the coefficient of determination.

    Args:
        classifier: Trained model.
        X_test: Testing data of independent features.
        y_test: Testing data for price.
    """
    # Perform standard scaling on the features
    scaler = StandardScaler()
    X_test = scaler.fit_transform(X_test)

    # Make predictions on the test set
    y_pred = classifier.predict(X_test)

    # Evaluate metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_pred)

    logger = logging.getLogger(__name__)
    logger.info("Accuracy: %.3f", accuracy)
    logger.info("Precision: %.3f", precision)
    logger.info("Recall: %.3f", recall)
    logger.info("F1-score: %.3f", f1)
    logger.info("Roc Auc: %.3f", roc_auc)


def test_model(
    classifier: RandomForestClassifier, preprocessed_abandono_teste: pd.DataFrame
):
    """Calculates and logs the coefficient of determination.

    Args:
        classifier: Trained model.
        X_test: Testing data of independent features.
        y_test: Testing data for price.
    """
    # Perform standard scaling on the features
    scaler = StandardScaler()
    abandono_teste = scaler.fit_transform(preprocessed_abandono_teste)

    # Make predictions on the test set
    y_pred = classifier.predict(abandono_teste)
    y_pred = pd.DataFrame(y_pred, columns=["Exited"]).reset_index().rename(columns={"index": "RowNumber"})

    # Logger
    logger = logging.getLogger(__name__)
    logger.info("Prediction for test set complety.")
    logger.info("Prediction file stored at '/churn-prediction/data/07_model_output/resultado_teste.csv'")
    return y_pred