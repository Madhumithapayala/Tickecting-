import requests
import json

# ServiceNow instance information
instance_url = 'YOUR_INSTANCE_URL'
username = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'

# Ticket details
short_description = 'Short description of the issue'
description = 'Detailed description of the issue'
seal_id = 'SEAL_ID_OR_CONFIGURATION_ITEM'  # Provide the Seal ID or Configuration Item here

# Construct the URL for the ServiceNow REST API endpoint
url = f'{instance_url}/api/now/table/incident'

# Headers for the API request
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

# Body of the API request
data = {
    'short_description': short_description,
    'description': description,
    'cmdb_ci': seal_id  # Use 'cmdb_ci' for Configuration Item or Seal ID
}

# Make the API request to create the ticket
response = requests.post(url, auth=(username, password), headers=headers, data=json.dumps(data))

# Check if the request was successful
if response.status_code == 201:
    print('Ticket created successfully!')
    # Optionally, you can retrieve the ticket number from the response
    ticket_number = response.json()['result']['number']
    print('Ticket Number:', ticket_number)
else:
    print('Failed to create ticket. Status code:', response.status_code)
    print('Response:', response.text)

