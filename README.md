
# Udacity Machine Learning Engineer with Microsoft Azure Nanodegree
# Capstone Project: Telecom Customer Churn Predictor <br>
By: Thomas Choong

<br>

## Introduction
<br>
The telecom industry has always been a high-activity industry with many customers coming and going. There can be multiple reasons why a customer decides to leave a provider (better pricing and/or product elsewhere, poor service, better reliability, etc.). Key to any company/business is to retain their customers and prevent churners; it is most cost-efficient to keep an existing customer than trying to acquire a net-new prospect, therefore, it is critical for businesses/companies to identify their high-risk customers and address their potential issues before they've churned. <br>
<br>

This project will utilize data from Kaggle's Telecom Customer Dataset (Link: https://www.kaggle.com/blastchar/telco-customer-churn), I will be training the model on the aforementioned dataset with Azure's AutoML & Hyperdrive feature (classification training). <br>
After training, the best model will be selected and pushed to an endpoint to be consumed. The result should give the user 'Yes' or 'No' indicating whether they are high risk churners. 

This particular real-time API can open possibilities for internal teams to better service their customers:
- Frontline Reps can have insight to the specific customer
- Sales & Marketing may have the option to target these specific customers to prevent churn
- Finance could use this to potentially budget expenses, measure future churn, etc.

## Task
The task for this project is to clean, prepare the data for training utilizing both Azure's AutoML feature and Hyperdrive method (to perform hyperparameter tuning). Upon successful training, the best model from either the AutoML/Hyperdrive run will be registered and deployed to an endpoint where one can consume it (by entering JSON data and the resulting endpoint will return a 'Yes' or 'No' as to whether the entered data signifies it is a higher churner or not).
<br>
### Project Architecture
<img src='https://github.com/thomascjw30/ML-Engineer-Capstone-Project/blob/main/Screenshots/project%20architecture.png'>

## Dataset
This project will utilize data from Kaggle's Telecom Customer Dataset (Link: https://www.kaggle.com/blastchar/telco-customer-churn)<br>
This will be a classification model as I am training on whether a customer will churn or not. <br>
Before any training with the dataset, I've made sure to remove customerID field as I believe it will not impact anything as it is a unique variable to each account.
<br>
It has the following columns and the Y variable 'Churn' is 'Yes' or 'No'<br>
<br>
<font size = '9'>
customerID - Unique Customer Acct #<br>
gender - What gender is the acct holder<br>
SeniorCitizen - Is the acct holder a senior citizen<br>
Partner - Does the acct holder have a partner<br>
Dependents - How many dependents does the acct holder have<br>
tenure - how long (months) has the acct holder been with the company<br>
PhoneService - does the acct holder have phone service <br>
MultipleLines - does the acct holder have multiple lines<br>
InternetService - does the acct holder have internet service <br>
OnlineSecurity - does the acct holder have online security service <br>
OnlineBackup - does the acct holder have online backup service <br>
DeviceProtection - does the acct holder have device protection service <br>
TechSupport - does the acct holder have tech support service <br>
StreamingTV - does the acct holder have streaming TV service <br>
StreamingMovies - does the acct holder have streaming movies service <br>
Contract- is the acct holder on contract<br>
PaperlessBilling - is the acct holder subscribed to Paperless Billing<br>
PaymentMethod - what is the payment method of acct holder<br>
MonthlyCharges - What are the monthly charges the acct holder pays<br>
TotalCharges - What is the total amount an acct holder pays<br>
Churn - Did the acct holder churn (Y Variable)<br>
</font>

## Access
For Microsoft Azure access, I created my own trial account, Ms Azure was able to grant me 250 CAD credits and a full month of access.
<br>
For dataset access, I have downloaded the dataset and uploaded into github to directly connect to the flat file (<a href="https://raw.githubusercontent.com/thomascjw30/ML-Engineer-Capstone-Project/main/WA_Fn-UseC_-Telco-Customer-Churn.csv">link</a>).
<br><br>
For AutoML, I have referenced the file in the jupyter notebook (automl.ipynb).:
<img src='https://github.com/thomascjw30/ML-Engineer-Capstone-Project/blob/main/Screenshots/data_access_automl.png'>
<br><br>
For Hyperdrive, I have reference the file in the train.py script: 
<img src='https://github.com/thomascjw30/ML-Engineer-Capstone-Project/blob/main/Screenshots/data_access_trainpy.png'>



## Automated ML
AutoML is a feature built in Microsoft Azure ML studio, it an automated process/feature where it reads in the dataset, run multiple iterations with various algorithms. After a number of runs, it will produce the best model depending on the criteria being measured (it can be accuracy, recall, precision, AUC, MAE, MSE, etc.).
<br>
For my dataset, I have selected Accuracy as the main criteria for determining the best model (as it is a binary classification model). <br>
Additionally, I set timeout to 30 minutes and max_concurrent_iterations to 10 (since I did not want to wait too long and it is a trial account with no additional cost on my end).
<br>
The Y-Variable is 'Churn' - as I am predicting whether an account will likely churn or not.

<img src='https://github.com/thomascjw30/ML-Engineer-Capstone-Project/blob/main/Screenshots/automl_settings.png'>
The best performing algorithmn for my dataset was VotingEnsemble (w/ 80.9% accuracy).
<img src='https://github.com/thomascjw30/ML-Engineer-Capstone-Project/blob/main/Screenshots/automl_widget_run_detail.png'>
<br>
The properties of the best performing model from AutoML (Voting Ensemble Model)
<img src='https://github.com/thomascjw30/ML-Engineer-Capstone-Project/blob/main/Screenshots/auto_bestmodel_features.png'>
<br>
<img src='https://github.com/thomascjw30/ML-Engineer-Capstone-Project/blob/main/Screenshots/automl_best_model_gui.png'>


## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search


### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
