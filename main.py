import os
import requests
import datetime as dt
# ---------------------------- CONSTANTS  ------------------------------- #
app_id = os.environ.get("APP_ID")
api_key = os.environ.get("API_KEY")

AGE = "24"
WEIGHT = 75
HEIGHT = 175
GENDER = "male"

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
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=api_endpoint, json=api_parameters, headers=api_headers)
response.raise_for_status()
exercise_data = response.json()


# ---------------------------- Google Sheets data ------------------------------- #
sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")
sheety_user_name = os.environ.get("SHEETY_USERNAME")
sheety_password = os.environ.get("SHEETY_PASSWORD")

date = dt.datetime.today().strftime("%d/%m/%Y")
time = dt.datetime.now().strftime("%X")
# ---------------------------- Updating google sheets ------------------------------- #

for exercise in exercise_data["exercises"]:
    new_row_data = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": str(exercise["duration_min"]),
            "calories": exercise["nf_calories"]
        }
    }

    print(exercise["duration_min"])
    add_row_response = requests.post(url=sheety_endpoint, json=new_row_data, auth=(sheety_user_name, sheety_password))
    add_row_response.raise_for_status()
