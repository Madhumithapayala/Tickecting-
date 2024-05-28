import requests
import json
import base64

# Apigee base URL
apigee_base_url = 'YOUR_APIGEE_BASE_URL'

# ServiceNow endpoint
incident_endpoint = '/api/now/table/incident'

# ServiceNow instance information
username = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'

# Construct the URL for the ServiceNow REST API endpoint
url = f'{apigee_base_url}{incident_endpoint}'

# Headers for the API request
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

# Create the base64-encoded credentials string
credentials = f'{username}:{password}'
credentials_bytes = credentials.encode('ascii')
credentials_base64 = base64.b64encode(credentials_bytes).decode('ascii')

# Include the Authorization header with the base64-encoded credentials
headers['Authorization'] = f'Basic {credentials_base64}'

# Body of the API request
data = {
    'short_description': 'Short description of the issue',
    'description': 'Detailed description of the issue',
    'cmdb_ci': 'SEAL_ID_OR_CONFIGURATION_ITEM'
}

# Make the API request to create the ticket
response = requests.post(url, headers=headers, data=json.dumps(data))

# Check if the request was successful
if response.status_code == 201:
    print('Ticket created successfully!')
else:
    print('Failed to create ticket. Status code:', response.status_code)
    print('Response:', response.text)
