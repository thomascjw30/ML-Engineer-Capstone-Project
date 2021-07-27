
# Udacity Machine Learning Engineer with Microsoft Azure Nanodegree
# Capstone Project: Telecom Customer Churn Predictor By: Thomas Choong


# Introduction
The telecom industry has always been a high-activity industry with many customers coming and going. There can be multiple reasons why a customer decides to leave a provider (better pricing and/or product elsewhere, poor service, better reliability, etc.). Key to any company/business is to retain their customers and prevent churners; it is more cost-efficient to keep an existing customer than trying to acquire a net-new prospect. Therefore, it is key for many businesses/companies to identify their high-risk customers and address their potential issues before they've churned. 
This project will utilize data from Kaggle's Telecom Customer Dataset (Link: https://www.kaggle.com/blastchar/telco-customer-churn), I will be training the model on the aforementioned dataset with Azure's AutoML & Hyperdrive feature. 
After training, the best model will be selected and pushed to an endpoint to be consumed. The result should give the user 'Yes' or 'No' indicating whether they are high risk churners. 

This particular real-time API can open possibilities for internal teams to better service the customers:
- Frontline Reps can have insight to the specific customer
- Sales & Marketing may have the option to target these specific customers to prevent churn


## Dataset
This project will utilize data from Kaggle's Telecom Customer Dataset (Link: https://www.kaggle.com/blastchar/telco-customer-churn)
It has the following columns and the Y variable 'Churn' is 'Yes' or 'No'
customerID - Unique Customer Acct #
gender - What gender is the acct holder
SeniorCitizen - Is the acct holder a senior citizen
Partner - Does the acct holder have a partner
Dependents - How many dependents does the acct holder have
tenure - how long (months) has the acct holder been with the company
PhoneService - does the acct holder have phone service 
MultipleLines - does the acct holder have multiple lines
InternetService - does the acct holder have internet service 
OnlineSecurity - does the acct holder have online security service 
OnlineBackup - does the acct holder have online backup service 
DeviceProtection - does the acct holder have device protection service 
TechSupport - does the acct holder have tech support service 
StreamingTV - does the acct holder have streaming TV service 
StreamingMovies - does the acct holder have streaming movies service 
Contract- is the acct holder on contract
PaperlessBilling - is the acct holder subscribed to Paperless Billing
PaymentMethod - what is the payment method of acct holder
MonthlyCharges - What are the monthly charges the acct holder pays
TotalCharges - What is the total amount an acct holder pays
Churn - Did the acct holder churn (Y Variable)
![image](https://user-images.githubusercontent.com/58406063/127240350-c8566d4f-1a3b-476a-ae24-07d695156cc7.png)


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
