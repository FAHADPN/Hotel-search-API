import requests
import json

# Replace with your API endpoint URL
api_url = 'http://127.0.0.1:8000/api/hotel_url/'

# Define the input data as a dictionary
data = {
    'destination': 'New York',           # Replace with your destination
    'check_in_date': '2023-09-15',       # Replace with your check-in date
    'check_out_date': '2023-09-20',      # Replace with your check-out date
}

# Make a POST request to the API
response = requests.post(api_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

# Check the response
if response.status_code == 200:
    result = response.json()
    kayak_url = result.get('url')
    print(f'Generated Kayak URL: {kayak_url}')
else:
    print(f'Error: {response.status_code} - {response.text}')
