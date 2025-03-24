import streamlit as st

def converter_units(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001,   # 1 meter = 0.001 kilometer
        "kilometers_meters": 1000,    # 1 kilometer = 1000 meters
        "grams_kilograms": 0.001,     # 1 gram = 0.001 kilogram
        "kilograms_grams": 1000       # 1 kilogram = 1000 grams
    }

    key = f"{unit_from}_{unit_to}"  # Generate a key based on input and output units

    if key in conversions:
        return value * conversions[key]
    else:
        return "Conversion not supported"

st.title("Unit Converter")

value = st.number_input("Enter the Value:", min_value=0.0, format="%.2f")

unit_from = st.selectbox("Convert from:", ["meters", "kilometers", "grams", "kilograms"])
unit_to = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms"])

if st.button("Convert"):
    if value is not None:
        result = converter_units(value, unit_from, unit_to)
        st.write(f"Converter value: {result}")
    else:
        st.write("Please enter a valid number.")

        
 