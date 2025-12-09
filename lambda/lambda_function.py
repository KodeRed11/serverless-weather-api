import json
import os
import urllib.request

def lambda_handler(event, context):
    city = event.get('city', 'London')

    api_key = os.getenv('OPENWEATHER_KEY')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
            weather = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description']
            }
            return {
                'statusCode': 200,
                'body': json.dumps(weather)
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }