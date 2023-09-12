# Hotel-search-API

This project contains the API for generating links that redirect you to the search results of Kayak.co.in website based on the date and destination of your choice. This helps you to create HyperLinks in your website or bots based on user choice of destination, check-in and check-out dates.

# How to run
### Installing Packages
1. First step is make sure you have proper version of python<br><br>Check your python version:<br>
```sh
python --version
```

2. Clone the repository to your local Machine<br><br> Cloning Repository
```sh
git clone https://github.com/FAHADPN/Hotel-search-API.git
```

3. Now install all the packages using following command:<br>
```sh
pip install -r requirements.txt
```
4. Now you make migrations and also migrate:
```sh
python manage.py makemigrations
python manage.py migrate
```

5. Now that you have successfully migrated now you are ready to localhost the api. Use following command to run server:
```sh
python manage.py runserver
```

6. Now the API will be running in the port 8000:
```sh
'http://127.0.0.1:8000/api/hotel_url/'
```
```sh
'http://localhost:8000/api/hotel_url/'
```

7. The example json format of API request:
```sh
data = {
    'destination': 'New York',           # Replace with your destination
    'check_in_date': '2023-09-15',       # Replace with your check-in date
    'check_out_date': '2023-09-20',      # Replace with your check-out date
}

```

8. You can check if the API is properly working by using the following [python code](https://github.com/FAHADPN/Hotel-search-API/blob/main/api-test.py)

```sh
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

```

# Conclusion

This project will help you as a starting point to building APIs using Django. Also helps you generate links for hotels in a particular area.

# For help & support

contact : <br><br>LinkedIn: [Fahad P N](https://www.linkedin.com/in/fahadpn)
<br> mail: [fahadpuzhakkaraillath@gmail.com](mailto:fahadpuzhallaraillath@gmail.com)