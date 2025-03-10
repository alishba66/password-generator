import streamlit as st
import random
import string

# Function to generate a password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Include uppercase and lowercase letters

    if use_digits:
        characters += string.digits  # Add digits if selected

    if use_special:
        characters += string.punctuation  # Add special characters if selected

    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit UI
st.title("🔐 Password Generator")

# User input for password criteria
length = st.slider("Select Password Length", min_value=6, max_value=20, value=12)
use_digits = st.checkbox("Include Digits")
use_special = st.checkbox("Include Special Characters")

# Generate button
if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.success(f"Generated Password: `{password}`")  # Displays password with success message

# Footer
st.write("Built by [Alishba Qureshi](https://github.com/alishba66)")
