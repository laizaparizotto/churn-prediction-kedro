# Data Science Challenge - Churn Prediction

This is a Kedro repository that tackles a data science challenge: **predicting customer churn** for a fictional financial institution. The goal is to build an effective Machine Learning pipeline using two datasets to accurately forecast customer churn. 

To approach this problem, it was first developed EDA, feature engineering and model training and evaluation using Jupyter Notebooks. The notebooks are located in `"kedro-environment-churn-prediction/churn-prediction/notebooks/"`. Feel free to visit the notebooks and check my reasoning behind the solution before running the pipeline. :)

[Exaploratory Data Analysis](churn-prediction/notebooks/EDA.ipynb)
[Feature Engineering](churn-prediction/notebooks/feature_engineering.ipynb)
[Model Training and Evaluation](churn-prediction/notebooks/model_training.ipynb)


### Data Understanding:
- The first dataset, named "Abandono_clientes" contains 10,000 rows and 13 columns, including a target column "Exited" with binary data (1 if the customer has churned, 0 if not). 
- The second dataset, named "Abandono_teste", consists of 1,000 rows and 12 columns, excluding the "Exited" column. 

### Key Concepts:
**Customer Churn:** Churn refers to the phenomenon of customers discontinuing their relationship with a company or service. In this context, it represents customers who have abandoned the financial institution.

**Features:** The dataset contains various features or attributes that provide information about the customers. Features include `Row Number`, `Customer Id`, `Surname`, `Credit Score`, `Geography`, `Gender`, `Age`, `Tenure` _(duration of the customer's relationship with the bank)_, `Balance`, `Number of Products Held`, `Has a Credit Card`, `Is Active Member` and `Estimated salary`.

**Exited:** The target variable `Exited` indicates whether a customer has churned (1) or not (0).

**Performance Metrics:** To assess the effectiveness of the model, various evaluation metrics are used, including accuracy, precision, recall, F1-score, and AUC-ROC curve. These metrics help gauge the model's predictive capability and its ability to correctly identify customers who are likely to churn.


## Getting started
Please note that this project was initially developed using Python 3.10.6 and on the Ubuntu operating system. 


**Clone the repository**

To clone the repository and set up the development environment, follow the steps below:

1. Clone the repository using the command:
   ```
   git clone https://github.com/laizaparizotto/kedro-environment-churn-prediction.git
   ```

2. Change to the cloned repository directory:
   ```
   cd kedro-environment-churn-prediction
   ```

3. Create a virtual environment using `venv`:
   ```
   python -m venv .venv
   ```

4. Activate the virtual environment:
   - For Windows:
     ```
     .venv\Scripts\activate
     ```
   - For macOS and Linux:
     ```
     source .venv/bin/activate
     ```

Now you have successfully cloned the repository and set up the virtual environment. You can proceed with the next steps as described in the project documentation.


**Install Kedro**

To install Kedro, run:
For more information, please check [Kedro Installation Documentation](https://docs.kedro.org/en/stable/get_started/install.html)

```
cd churn-prediction/
pip install kedro
```


**Install dependencies**

All necessary dependencies are located in `src/requirements.txt`.

To install them, run:

```
pip install -r src/requirements.txt
```

## How to run your Kedro pipeline

You can run the Kedro project with:

```
kedro run
```

## How to test your Kedro project

Have a look at the file `src/tests/test_run.py` for instructions on how to write your tests. You can run your tests as follows:

```
kedro test
```

## Interactive Visualization

You can acess the interactive visualization with

```
kedro viz
```
