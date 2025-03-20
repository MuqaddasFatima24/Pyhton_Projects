import streamlit as st
import time

# Set page configuration
st.set_page_config(page_title="Unit Converter", layout="wide", initial_sidebar_state="expanded")

# Add custom CSS for fonts and glow effects
st.markdown("""
    <style>
        /* Resetting background to white */
        .stApp {
            background-color: #ffffff;
            color: #333;
        }

        /* Customize the title */
        .stTitle {
            font-family: 'Lobster', sans-serif;
            font-size: 35px;
            color: #9b4dca;  /* Purple color */
            text-align: center;
            margin-bottom: 20px;
        }

        /* Style the selectbox and number inputs with glow effect */
        .stSelectbox, .stNumberInput {
            font-size: 18px;
            padding: 10px;
            border-radius: 5px;
            border: 2px solid #9b4dca;  /* Purple border */
            transition: all 0.3s ease;
        }

        /* Adding glow effect on focus */
        .stSelectbox:focus, .stNumberInput:focus {
            box-shadow: 0 0 10px rgba(155, 77, 202, 0.7); /* Glow effect */
            border-color: #9b4dca;
        }

        /* Customize buttons with glow effect */
        .stButton > button {
            background-color: #9b4dca;  /* Purple button */
            color: white;
            padding: 15px 30px;
            font-size: 16px;
            border-radius: 8px;
            border: none;
            transition: all 0.3s ease;
        }

        .stButton > button:hover {
            background-color: #7b2ab1;  /* Darker purple on hover */
            box-shadow: 0 0 15px rgba(155, 77, 202, 1); /* Glow effect on hover */
        }

        .stButton > button:active {
            transform: scale(0.98); /* Scale effect when clicked */
        }

        /* Add custom fonts */
        @import url('https://fonts.googleapis.com/css2?family=Lobster&display=swap');

        /* Subtitle styling */
        h2 {
            font-family: 'Open Sans', sans-serif;
            font-size: 22px;
            color: #9b4dca;  /* Purple color for subtitle */
        }

        /* Customize the footer or author section */
        .author-section {
            margin-top: 40px;
            text-align: center;
            font-size: 14px;
            color: #333;
        }

        .author-section a {
            color: #9b4dca;
        }

        /* Custom styles for selectbox focus (when clicked) */
        .stSelectbox:focus {
            border-color: #9b4dca;
            box-shadow: 0 0 5px rgba(155, 77, 202, 0.8);
        }

        /* Active state for selected items */
        .stSelectbox option:checked {
            background-color: #9b4dca;
            color: white;
        }

        .stSelectbox .css-1s2u09g {
            background-color: #9b4dca;
        }
    </style>
""", unsafe_allow_html=True)

# Add heading for the page
st.title("🔮 **Unit Converter**")
st.markdown("Welcome to the **Unit Converter**. Convert various units easily with a sleek purple theme!")

# Conversion rates dictionary
conversion_rates = {
    "length": {
        "kilometers": 1,
        "meters": 1000,
        "centimeters": 100000,
        "millimeters": 1000000,
        "miles": 0.621371,
        "yards": 1093.61,
        "inches": 39370.1
    },
    "weight": {
        "kilograms": 1,
        "grams": 1000,
        "milligrams": 1000000,
        "pounds": 2.20462,
        "ounces": 35.274
    },
    "temperature": {
        "celsius": 1,
        "fahrenheit": lambda x: (x * 9/5) + 32,
        "kelvin": lambda x: x + 273.15
    },
    "volume": {
        "liters": 1,
        "milliliters": 1000,
        "gallons": 0.264172,
        "cups": 4.22675,
        "pints": 2.11338
    },
    "speed": {
        "meters_per_second": 1,
        "kilometers_per_hour": 3.6,
        "miles_per_hour": 2.23694,
        "feet_per_second": 3.28084
    },
    "time": {
        "seconds": 1,
        "minutes": 60,
        "hours": 3600,
        "days": 86400
    },
    "energy": {
        "joules": 1,
        "kilojoules": 1000,
        "calories": 0.239006,
        "kilocalories": 0.000239006
    }
}

# Function to convert between different units
def convert_units(value, from_unit, to_unit, category):
    if category == "temperature":
        if isinstance(conversion_rates[category][from_unit], float):
            value_in_base = value * conversion_rates[category][from_unit]
        else:
            value_in_base = conversion_rates[category][from_unit](value)

        if isinstance(conversion_rates[category][to_unit], float):
            result = value_in_base / conversion_rates[category][to_unit]
        else:
            result = conversion_rates[category][to_unit](value_in_base)
    else:
        value_in_base = value * conversion_rates[category][from_unit]
        result = value_in_base / conversion_rates[category][to_unit]

    return result

# UI for selecting the category of conversion
category = st.selectbox("Select the category of conversion", list(conversion_rates.keys()))

# UI for input
st.write("💡 Choose the value, and select the units you want to convert.")

col1, col2 = st.columns(2)

with col1:
    value = st.number_input("Enter the value to convert", min_value=0.01, format="%.2f")

with col2:
    from_unit = st.selectbox(f"From {category.capitalize()} Unit", list(conversion_rates[category].keys()))

# Dropdown for 'to' units
to_unit = st.selectbox(f"To {category.capitalize()} Unit", list(conversion_rates[category].keys()))

# Add a loading spinner for conversions
with st.spinner('Working on your conversion... Please wait!'):
    time.sleep(2)  # Simulate a small delay

# Convert and display result
if st.button("Convert"):
    if value > 0:
        result = convert_units(value, from_unit, to_unit, category)
        st.success(f"✅ {value} {from_unit} is equal to {result:.2f} {to_unit}")
    else:
        st.error("❌ Please enter a valid number greater than 0.")

# Author Section (About the Creator)
st.markdown("""
    <div class="author-section">
        Made with ❤️ by <a href="https://github.com/MuqaddasFatima24">Muqaddas Fatima</a>. 
        Check out my GitHub for more awesome projects!
    </div>
""", unsafe_allow_html=True)
