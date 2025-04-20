import streamlit as st

st.title("🔄 Unit Converter")
st.write("Convert between different units of Length, Temperature, and Mass using Python + Streamlit!")

conversion_type = st.selectbox("Select conversion type", ["Length", "Temperature", "Mass"])

if conversion_type == "Length":
    units = ["kilometers", "meters", "centimeters", "inches"]
    conversions = {
        "kilometers": 0.001,
        "meters": 1,
        "centimeters": 100,
        "inches": 39.3701
    }
elif conversion_type == "Temperature":
    units = ["celsius", "fahrenheit", "kelvin"]
elif conversion_type == "Mass":
    units = ["kilograms", "grams"]
    conversions = {
        "kilograms": 1,
        "grams": 1000
    }

from_unit = st.selectbox("Convert from:", units)
to_unit = st.selectbox("Convert to:", units)
value = st.number_input("Enter the value:", min_value=0.0 )


def convert_units(value, convert_from, convert_to, conversion_type):
    if conversion_type == "Length" or conversion_type == "Mass":
        base_value = value / conversions[convert_from]
        return base_value * conversions[to_unit]
    elif conversion_type == "Temperature":
        if convert_from == convert_to:
            return value
        elif convert_from == "celsius":
            if convert_to == "fahrenheit":
                return (value * 9/5) + 32
            elif convert_to == "kelvin":
                return value + 273.15
        elif convert_from == "fahrenheit":
            if convert_to == "celsius":
                return (value - 32) * 5/9
            elif convert_to == "kelvin":
                return ((value - 32) * 5/9) + 273.15
        elif convert_from == "kelvin":
            if convert_to == "celsius":
                return value - 273.15
            elif convert_to == "fahrenheit":
                return ((value - 273.15) * 9/5) + 32
    return "Conversion not supported"

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, conversion_type)
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
