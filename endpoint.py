import requests
import json

# URL for the web service, should be similar to:
# scoring_uri and key are found in the deployed model data and allow any api/web interface to access as req'd.
scoring_uri = 'http://d926a0b7-0a41-44a6-9a98-bec7b279fae8.eastus2.azurecontainer.io/score'
# If the service is authenticated, set the key or token
# key = 'Ptv8wKeDcTKCod1qO02pyaJRxZqksGf2'

# Endpoint.py is used to pass new data to the scoring uri as defined by the deployed model.  
# The format has to be in the format (wrangled,pipeline) as per the orignal model input
# Two sets of data to score, so we get two results back

# in the case of this dataset the original file included passing it through clean data, and the finalised clean data
# needs to be passed through to this model.  It is then encoded, again we need to pass new encoded information through.
# a simple way to find out how to interact with the model is to download the deployed model endpoint swagger ui (swagger.json)
# file into a swagger directory with the swagger.sh and serve.py python script.  The serve.py script allows the swagger run
# to access the local directory and enables access tl localhost:9000 and http://localhost:8000/swagger.json.  This will provide 
# examples of outputs which the below input data needs to match (post method)

# define data as required for the model.

# two sets of data to score
data = {"data":
        [
          {
	'gender' :'Female',
	'SeniorCitizen' :0,
	'Partner' :'Yes',
	'Dependents' :'No',
	'tenure' :1,
	'PhoneService' :'No',
	'MultipleLines' :'No phone service',
	'InternetService' :'DSL',
	'OnlineSecurity' :'No',
	'OnlineBackup' :'Yes',
	'DeviceProtection' :'No',
	'TechSupport' :'No',
	'StreamingTV' :'No',
	'StreamingMovies' :'No',
	'Contract' :'Month-to-month',
	'PaperlessBilling' :'Yes',
	'PaymentMethod' :'Electronic check',
	'MonthlyCharges' :29.85,
	'TotalCharges' :29.85,
          },
          {
	'gender' :'Male',
	'SeniorCitizen' :1,
	'Partner' :'Yes',
	'Dependents' :'Yes',
	'tenure' :1,
	'PhoneService' :'No',
	'MultipleLines' :'No phone service',
	'InternetService' :'DSL',
	'OnlineSecurity' :'Yes',
	'OnlineBackup' :'Yes',
	'DeviceProtection' :'Yes',
	'TechSupport' :'Yes',
	'StreamingTV' :'Yes',
	'StreamingMovies' :'Yes',
	'Contract' :'Month-to-month',
	'PaperlessBilling' :'Yes',
	'PaymentMethod' :'Electronic check',
	'MonthlyCharges' :50.50,
	'TotalCharges' :50.50,
          },
      ]
    }

# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
# headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())