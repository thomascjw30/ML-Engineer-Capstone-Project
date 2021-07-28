from sklearn.linear_model import LogisticRegression
import argparse
import os
import numpy as np
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from azureml.core.run import Run
from azureml.data.dataset_factory import TabularDatasetFactory
from azureml.core import Dataset
from azureml.core.run import Run
from azureml.data.dataset_factory import TabularDatasetFactory
from azureml.core import Dataset
from azureml.core import Dataset, Datastore
from azureml.data.datapath import DataPath
from sklearn.ensemble import RandomForestClassifier

# TODO: Create TabularDataset using TabularDatasetFactory
# Data is located at:
# "https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv"

url= "https://raw.githubusercontent.com/thomascjw30/ML-Engineer-Capstone-Project/main/WA_Fn-UseC_-Telco-Customer-Churn.csv"

ds = TabularDatasetFactory.from_delimited_files(path=url)
df =ds.to_pandas_dataframe()


def clean_data(data):
    
    # Dict for cleaning data
    i_service = {"DSL":1, "Fiber optic":2, "No":3}
    multi_lines = {"No phone service":1, "No":2, "Yes":3}
    contract = {'Month-to-month':1, 'One year':2, 'Two year':3}
    payment_method = {'Electronic check':1, 'Mailed check':2, 'Bank transfer (automatic)':3,'Credit card (automatic)':4}
    
    
    # Clean and one hot encode data
    x_df = data.to_pandas_dataframe().dropna()
    x_df["gender"] = x_df.gender.apply(lambda s: 1 if s == "Male" else 0)
    x_df["partner"] = x_df.Partner.apply(lambda s: 1 if s == True else 0)
    x_df["dependents"] = x_df.Dependents.apply(lambda s: 1 if s == True else 0)
    x_df["phoneservice"] = x_df.PhoneService.apply(lambda s: 1 if s == True else 0)
    x_df["onlinesecurity"] = x_df.OnlineSecurity.apply(lambda s: 1 if s == 'Yes' else 0)
    x_df["onlinebackup"] = x_df.OnlineBackup.apply(lambda s: 1 if s == 'Yes' else 0)
    x_df["deviceprotection"] = x_df.DeviceProtection.apply(lambda s: 1 if s == 'Yes' else 0)
    x_df["techsupport"] = x_df.TechSupport.apply(lambda s: 1 if s == 'Yes' else 0)
    x_df["streamingtv"] = x_df.StreamingTV.apply(lambda s: 1 if s == 'Yes' else 0)
    x_df["streamingmovies"] = x_df.StreamingMovies.apply(lambda s: 1 if s == 'Yes' else 0)
    x_df["paperbilling"] = x_df.PaperlessBilling.apply(lambda s: 1 if s == True else 0)
    
    x_df['internetservice'] = x_df.InternetService.map(i_service)
    x_df['multiplelines'] = x_df.MultipleLines.map(multi_lines)
    x_df['contract'] = x_df.Contract.map(contract)
    x_df['paymentmethod'] = x_df.PaymentMethod.map(payment_method)
    
    y_df = x_df[['Churn']]
    y_df["churn"] = y_df.Churn.apply(lambda s: 1 if s == True else 0)
    
    
    y_df.drop('Churn', inplace=True, axis=1)
    
    x_df.drop(['customerID', 'gender', 'SeniorCitizen', 'Partner', 'Dependents',
       'tenure', 'PhoneService', 'MultipleLines', 'InternetService',
       'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
       'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
       'PaymentMethod', 'MonthlyCharges', 'TotalCharges', 'Churn'], inplace=True, axis=1)

    
    return x_df, y_df

x, y = clean_data(ds)

# TODO: Split data into train and test sets.

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size =0.2, random_state=0)

# ## YOUR CODE HERE ###a

# run = Run.get_context()


# def main():
#     # Add arguments to script
#     parser = argparse.ArgumentParser()

#     parser.add_argument('--C', type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
#     parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations to converge")

#     args = parser.parse_args()

#     run.log("Regularization Strength:", np.float(args.C))
#     run.log("Max iterations:", np.int(args.max_iter))

#     model = LogisticRegression(C=args.C, max_iter=args.max_iter).fit(x_train, y_train)

#     accuracy = model.score(x_test, y_test)
#     run.log("Accuracy", np.float(accuracy))

def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--n_estimators', type=int, default=100, help="The number of trees in the forest.")
    parser.add_argument('--max_depth', type=int, default=10, help="The maximum depth of the tree.")

    args = parser.parse_args()

    run = Run.get_context()

    run.log("Number of Estimators:", np.float(args.n_estimators))
    run.log("Max iterations:", np.int(args.max_depth))

    model = RandomForestClassifier(n_estimators=args.n_estimators, max_depth=args.max_depth,random_state=42).fit(x_train, y_train)

    accuracy = model.score(x_test, y_test)
    run.log("Accuracy", np.float(accuracy))
    os.makedirs('outputs', exist_ok=True)
    joblib.dump(value=model, filename=f"./outputs/best_run_hyperdrive.pkl")


if __name__ == '__main__':
    main()


