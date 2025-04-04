import re
import random
import string
import streamlit as st
import qrcode
from io import BytesIO

# Optimized regex patterns for password checking
uppercase_pattern = re.compile(r"[A-Z]")
lowercase_pattern = re.compile(r"[a-z]")
digit_pattern = re.compile(r"\d")
special_char_pattern = re.compile(r"[!@#$%^&*]")
common_pattern = re.compile(r"(password|123|abc|qwerty|letmein)", re.IGNORECASE)

# Function to check password strength and return feedback
def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 12:
        score += 1
    else:
        feedback.append("❌ Password should be at least 12 characters long.")
    
    # Uppercase & Lowercase Check
    if uppercase_pattern.search(password) and lowercase_pattern.search(password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if digit_pattern.search(password):
        score += 1
    else:
        feedback.append("❌ Add at least one digit (0-9).")
    
    # Special Character Check
    if special_char_pattern.search(password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Common Word Check
    if common_pattern.search(password):
        feedback.append("❌ Your password contains common patterns. Try using more unique characters.")
    
    # Strength Rating
    strength = "Weak"
    if score == 4:
        strength = "Moderate"
    elif score == 5:
        strength = "Strong"
    feedback.append(f"✅ Password Strength: {strength}")
    
    return score, feedback

# Function to generate strong password
def generate_strong_password(length=12, use_digits=True, use_special=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += "!@#$%^&*"
    
    return ''.join(random.choice(characters) for _ in range(length))

# Function to create QR code for password
def generate_qr_code(data):
    qr = qrcode.make(data)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    return buffer.getvalue()

# Main app
st.set_page_config(page_title="Advanced Password Generator & Checker", layout="wide")
st.title("🔐 Advanced Password Generator & Strength Checker")

# Sidebar Settings
st.sidebar.header("Customize Your Password")
password_length = st.sidebar.slider("Select Password Length", 8, 30, 12)
include_digits = st.sidebar.checkbox("Include Digits", value=True)
include_special = st.sidebar.checkbox("Include Special Characters", value=True)

# Password Input
password = st.text_input("Enter your password to check strength:", type="password")
if password:
    score, feedback = check_password_strength(password)
    st.progress(score / 5)
    for message in feedback:
        st.write(message)
    if score < 5:
        st.warning("💡 Consider using a stronger password.")
        suggested_password = generate_strong_password(password_length, include_digits, include_special)
        st.write(f"Suggested Password: `{suggested_password}`")
        st.image(generate_qr_code(suggested_password), caption="Scan to save password")

# Password Generator
st.subheader("Generate a Secure Password")
if st.button("Generate Password"):
    new_password = generate_strong_password(password_length, include_digits, include_special)
    st.success(f"Generated Password: `{new_password}`")
    st.image(generate_qr_code(new_password), caption="Scan to save password")


