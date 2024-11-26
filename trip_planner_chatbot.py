import json
from flask import Flask, render_template, request, jsonify
import numpy as np
from tensorflow import keras
import pickle
import re
import requests

app = Flask(__name__)

# Load model, tokenizer, and label encoder with error handling
try:
    model = keras.models.load_model('chat_model.keras')
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    with open('label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)
except Exception as e:
    print(f"Error loading files: {e}")

# Load city data from JSON file
try:
    with open("city.json") as file:
        data = json.load(file)
except FileNotFoundError:
    print("city.json file not found. Ensure it's in the correct directory.")

def get_distance_locationiq(current_location, destination_location):
    api_key = "pk.f2ca5eb4c23d985723e09c5687812bcc"  # Replace with your free LocationIQ API key
    url = f"https://us1.locationiq.com/v1/matrix/driving/{current_location};{destination_location}?key={api_key}"

    print(f"Request URL: {url}")  # Debugging output

    try:
        response = requests.get(url)
        data = response.json()
        
        # Debugging output
        print("LocationIQ API response:", data)

        # Check for successful response
        if response.status_code == 200 and 'distances' in data:
            distance = data['distances'][0][1]  # Distance in meters
            return distance / 1000  # Convert to kilometers
        else:
            print("Error or missing data in LocationIQ response:", data)
    except Exception as e:
        print(f"Exception occurred: {e}")
        return None

# Dynamic budget calculation based on distance
def calculate_budgets_for_all_modes(distance):
    # Define the per-km rates for each mode of transport
    cost_per_km = {
        'car': 0.15,
        'bus': 0.1,
        'train': 0.08,
        'bike': 0.05
    }
    budgets = {mode: distance * rate for mode, rate in cost_per_km.items()}
    return budgets

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    print(f"User Message: {user_message}")

    try:
        # Predict intent
        max_len = 20
        padded_sequence = keras.preprocessing.sequence.pad_sequences(
            tokenizer.texts_to_sequences([user_message]),
            truncating='post', maxlen=max_len
        )
        result = model.predict(padded_sequence)
        tag = lbl_encoder.inverse_transform([np.argmax(result)])[0]

        response_data = []

        # Check if user is asking for budget calculation
        if "budget" in user_message.lower():
            # Extract current location and destination from user message
            match = re.search(r'from (.+?) to (.+?) by (.+)', user_message, re.IGNORECASE)
            if match:
                current_location = match.group(1).strip().replace(" ", "%20")  # URL encoding spaces
                destination_location = match.group(2).strip().replace(" ", "%20")

                # Get distance using the correct function
                distance = get_distance_locationiq(current_location, destination_location)
                if distance is not None:
                    # Calculate budget for all transport modes
                    budgets = calculate_budgets_for_all_modes(distance)
                    budget_text = "\n".join([f"{mode.capitalize()}: ${budget:.2f}" for mode, budget in budgets.items()])
                    
                    response_data.append({
                        "type": "text",
                        "text": f"The estimated budgets from {current_location.replace('%20', ' ')} to {destination_location.replace('%20', ' ')} are:\n{budget_text}"
                    })
                else:
                    response_data.append({"type": "error", "text": "Could not retrieve distance information. Please check your locations."})
            else:
                response_data.append({"type": "error", "text": "Please provide a valid format: 'Calculate budget from [current location] to [destination] by [transport mode]'."})

        # Handle other chatbot functionalities (e.g., city information)
        elif tag == 'city_info':
            city = extract_city_name(user_message)
            city_data = data['intents'][2]['data'].get(city)

            if city_data:
                # Example response logic for city info
                response_data.append({
                    "type": "text",
                    "text": f"Here is information for {city.title()}: {city_data}"
                })
            else:
                response_data.append({"type": "error", "text": f"Sorry, I couldn't find information for the city '{city}'."})

        # General fallback for other intents
        else:
            response_data.append({"type": "error", "text": "Sorry, I didn't understand that."})

        return jsonify(response_data)

    except Exception as e:
        print(f"Error: {e}")
        return jsonify([{"type": "error", "text": f"Oops! There was an error processing your request: {e}"}])

if __name__ == '__main__':
    app.run(debug=True)
