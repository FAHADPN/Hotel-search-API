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



