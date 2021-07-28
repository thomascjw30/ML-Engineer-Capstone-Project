
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

This particular real-time API can open possibilities for internal teams to better service the customers:
- Frontline Reps can have insight to the specific customer
- Sales & Marketing may have the option to target these specific customers to prevent churn

## Project Architecture
<img src='https://github.com/thomascjw30/ML-Engineer-Capstone-Project/blob/main/Screenshots/project%20architecture.png'>

## Dataset
This project will utilize data from Kaggle's Telecom Customer Dataset (Link: https://www.kaggle.com/blastchar/telco-customer-churn)<br>
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

### Overview
*TODO*: Explain about the data you are using and where you got it from.

### Task
*TODO*: Explain the task you are going to be solving with this dataset and the features you will be using for it.

### Access
*TODO*: Explain how you are accessing the data in your workspace.

## Automated ML
*TODO*: Give an overview of the `automl` settings and configuration you used for this experiment

### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

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
