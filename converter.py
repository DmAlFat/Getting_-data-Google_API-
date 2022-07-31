import requests  # Connect the module to send all kinds of HTTP requests

# execute the corresponding request and write the necessary information to the course variable
data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
course = data['Valute']['USD']['Value']
