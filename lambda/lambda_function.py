import json
import os
import urllib.request

def lambda_handler(event, context):
    city = event.get("queryStringParameters", {}).get("city", "Phoenix")

    api_key = os.environ["OPENWEATHER_KEY"]
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
            return {
                "statusCode": 200,
                "body": json.dumps({
                    "city": city,
                    "temperature": data["main"]["temp"],
                    "weather": data["weather"][0]["description"]
                })
            }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
