import streamlit as st
import random
import string
import time

# Function to check password strength
def check_password_strength(password):
    length = len(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for c in password)
    
    score = sum([has_lower, has_upper, has_digit, has_special])
    
    if length < 6:
        return "Weak", "red"
    elif length < 10 and score >= 2:
        return "Moderate", "orange"
    elif length >= 10 and score >= 3:
        return "Strong", "green"
    else:
        return "Very Strong", "blue"

# Function to generate a strong password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))

# Function to calculate password entropy
def calculate_entropy(password):
    charset_size = 0
    if any(c.islower() for c in password): charset_size += 26
    if any(c.isupper() for c in password): charset_size += 26
    if any(c.isdigit() for c in password): charset_size += 10
    if any(c in string.punctuation for c in password): charset_size += len(string.punctuation)
    
    if charset_size == 0:
        return 0
    return len(password) * (charset_size.bit_length())

# Function to estimate time to crack the password
def time_to_crack(entropy):
    seconds = 2 ** entropy / 1e9  # Assume a billion guesses per second
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        return f"{seconds / 60:.2f} minutes"
    elif seconds < 86400:
        return f"{seconds / 3600:.2f} hours"
    elif seconds < 31536000:
        return f"{seconds / 86400:.2f} days"
    else:
        return f"{seconds / 31536000:.2f} years"

# Function to check for common passwords
def is_common_password(password):
    common_passwords = {"123456", "password", "123456789", "qwerty", "abc123", "password1", "123123"}
    return password in common_passwords

# Function to suggest improvements
def suggest_improvements(password):
    suggestions = []
    if len(password) < 12:
        suggestions.append("Increase the password length.")
    if not any(c.islower() for c in password):
        suggestions.append("Add lowercase letters.")
    if not any(c.isupper() for c in password):
        suggestions.append("Add uppercase letters.")
    if not any(c.isdigit() for c in password):
        suggestions.append("Include numbers.")
    if not any(c in string.punctuation for c in password):
        suggestions.append("Use special characters.")
    return suggestions

# Streamlit UI 
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐", layout="centered")

st.title("🔐 Password Strength Meter")
password = st.text_input("Enter your password:", type="password")

if password:
    strength, color = check_password_strength(password)
    entropy = calculate_entropy(password)
    crack_time = time_to_crack(entropy)
    
    st.markdown(f"**Strength:** <span style='color:{color}; font-weight:bold'>{strength}</span>", unsafe_allow_html=True)
    st.write(f"🔢 **Entropy Score:** {entropy:.2f} bits")
    st.write(f"⏳ **Estimated Time to Crack:** {crack_time}")
    
    if is_common_password(password):
        st.error("❌ This password is too common! Choose a more unique password.")
    
    improvements = suggest_improvements(password)
    if improvements:
        st.warning("💡 Suggestions to Improve Your Password:")
        for suggestion in improvements:
            st.write(f"- {suggestion}")
    
    if strength == "Weak":
        st.warning("⚠️ Your password is weak! Consider using a mix of uppercase, lowercase, numbers, and symbols.")
    elif strength == "Moderate":
        st.info("ℹ️ Your password is okay, but could be stronger.")
    elif strength == "Strong":
        st.success("✅ Great! Your password is strong.")
    else:
        st.balloons()
        st.success("🎉 Excellent! Your password is very strong.")

# Password generator section with styling
st.subheader("🔑 Generate a Secure Password")
password_length = st.slider("Select password length:", min_value=8, max_value=32, value=12)
if st.button("Generate Strong Password"):
    strong_password = generate_password(password_length)
    st.text(f"🔹 Suggested Password: {strong_password}")
    st.write("🔹 **Tip:** Use a password manager to store your strong passwords securely.")

st.markdown("<h4 style='text-align: center;'> Made with ❤️ by ahsen adil</h4>", unsafe_allow_html=True)