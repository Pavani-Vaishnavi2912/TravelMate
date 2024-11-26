# TravelMate
Your Ultimate Travel Companion

**TravelMate** is an AI-powered tourism chatbot designed to revolutionize the travel planning experience. This intelligent chatbot helps users by providing personalized travel recommendations, budget estimations, and real-time information about accommodations, dining options, and local attractions.

---

## Features 🚀
- **Personalized Recommendations**: Get tailored suggestions for destinations, accommodations, dining, and attractions based on your preferences.
- **Budget Planning**: Accurate cost estimations for travel, accommodation, and dining based on real-time inputs.
- **City-Specific Information**: Detailed data for 30+ cities, including descriptions, images, and budgets.
- **Interactive Chat Interface**: Intuitive, user-friendly chatbot for seamless interaction.
- **Real-Time Distance and Budget Calculations**: Supports various transportation modes like bike, car, and bus.
- **Dynamic Dataset Integration**: Uses a structured JSON dataset for accurate and updated travel insights.

---

## Technology Stack 🛠️
- **Programming Language**: Python
- **Backend Framework**: Flask
- **Machine Learning**: TensorFlow/Keras for intent classification and prediction
- **Frontend**: HTML/CSS (integrated with Flask)
- **Database**: MySQL & JSON-based datasets
- **APIs**: Google Maps API, Geopy for geolocation services
- **Testing Framework**: Unit, Integration, System, and Acceptance Testing

---

## System Design 🖥️
1. **Chatbot UI**: Simple and responsive web-based interface.
2. **Machine Learning Model**: Pre-trained neural network for understanding and classifying user intents.
3. **Backend Logic**: Flask routes handling data queries and responses.
4. **Database**: JSON for city datasets and MySQL for user authentication data.
5. **Distance Calculation Module**: Geopy integration for geolocation and dynamic travel cost computation.
---

## Installation 📥

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/TravelMate.git
   cd TravelMate
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: .\env\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Database**:
   - Update database settings in `config.py`.
   - Import `city.json` as the dataset for city-specific information.

5. **Run the Application**:
   ```bash
   python travelmate.py
   ```
   Access the app at `http://127.0.0.1:5000`.

---

## Usage Guide 📚

1. **Register/Login**:
   - Sign up with your credentials.
   - Login to access personalized features.

2. **Chat with the Bot**:
   - Ask questions like:
     - "What can I visit in Hyderabad?"
     - "What dining options are available in Chennai?"
     - "What is the travel cost from Bangalore to Mysore by car?"

3. **Explore Recommendations**:
   - Get suggestions with descriptions, images, and budget details.

4. **Plan Your Budget**:
   - Use the chatbot to calculate travel costs for different transportation modes.

---

## Future Enhancements 🌟
- **API Integration**: Fetch live data for accommodations and attractions.
- **Language Support**: Add multilingual support with real-time translation.
- **Voice Interaction**: Integrate speech-to-text for voice-based queries.
- **Booking Features**: Allow direct booking for accommodations and activities.

---
