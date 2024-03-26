import streamlit as st
import random
import string

# Function to generate password
def generate_password(length):
    # Define characters to be used for password generation
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate password using random choice from defined characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to display password strength with colors
def display_strength(password):
    strength = "Weak"
    if len(password) >= 12 and any(c.islower() for c in password) and any(c.isupper() for c in password) and any(c.isdigit() for c in password):
        strength = "Strong"
    elif len(password) >= 8:
        strength = "Medium"
    return strength

def main():
    st.set_page_config(page_title="Password Generator", page_icon="🔐")

    st.title("🔐 Password Generator 🔐")

    # User input for password length
    password_length = st.slider("Select the desired length of the password:", min_value=6, max_value=50, value=12, step=1)

    # Generate password
    password = generate_password(password_length)

    # Display password
    st.markdown(f"## 🎉 Your Generated Password:")
    st.markdown(f"### ✨ {password}")

    # Display password strength with colors
    password_strength = display_strength(password)
    if password_strength == "Weak":
        st.markdown(f"### 💪 Password Strength: <span style='color:red'>{password_strength}</span>", unsafe_allow_html=True)
    elif password_strength == "Medium":
        st.markdown(f"### 💪 Password Strength: <span style='color:orange'>{password_strength}</span>", unsafe_allow_html=True)
    else:
        st.markdown(f"### 💪 Password Strength: <span style='color:green'>{password_strength}</span>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()

    st.divider()
    st.write(
            """
            Made with ❤️ By **_Jaweria Batool_** 
            """
        )

    # link to GitHub README file
    st.write("For more information about how the app works, please check out the [GitHub README](https://github.com/Jaweria-B/codsoft/tree/main/task-3/pass-gen) file.")

