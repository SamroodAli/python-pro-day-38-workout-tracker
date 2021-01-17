import os
import requests

# ---------------------------- CONSTANTS  ------------------------------- #
app_id = os.environ.get("APP_ID")
api_key = os.environ.get("API_KEY")

# ---------------------------- NUTRITIONIX API ENDPOINT and Headers ------------------------------- #
api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

api_headers = {
    "x-app-id": app_id,
    "x-app-key": api_key,
    "Content-Type": "application/json"
}


# ---------------------------- RUNNING THE PROGRAM  ------------------------------- #
user_input = input("Tell me which excercises you did: ")

api_parameters = {
    "query": user_input,
    "gender": "male",
    "weight_kg": 75,
    "height_cm": 175,
    "age": 24
}

response = requests.post(url=api_endpoint, json=api_parameters, headers=api_headers)
response.raise_for_status()
exercise_data = response.json()