import streamlit as st
import random
import time

# Dictionary containing image paths for each choice
images = {
    "rock": "./assets/rock.png",      
    "paper": "./assets/paper.png",     
    "scissors": "./assets/scissors.png"   
}

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        st.warning("It's a tie! 😊")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        st.success("You win! 🎉")
    else:
        st.error("You lose! 😔")

def main():
    st.set_page_config(page_title="Rock-Paper-Scissors", page_icon="./assets/rock-paper-scissors.png")  # Set page title and icon
    st.title("Rock-Paper-Scissors Game")

    # First row: User's choice and computer's choice
    col1, col2 = st.columns(2)
    col1.markdown(f"### Your Choice: 👤")
    user_choice = col1.radio("", ["rock", "paper", "scissors"], key="user_choice")
    
    with col2:
        if user_choice:
            st.markdown(f"### Computer's Choice: 🤖")
            with st.spinner("Loading..."):
                time.sleep(1)  # Simulating image loading delay
                computer_choice = random.choice(['rock', 'paper', 'scissors'])
                col2.markdown(f"* ### <span style='color:white'>{computer_choice.title()}</span>", unsafe_allow_html=True)

    # Second row: Image cards for user's and computer's choices
    st.write("Comparision")
    col1, col2 = st.columns(2)
    if user_choice:
        with st.spinner("Loading..."):
            time.sleep(1)  # Simulating image loading delay
            col1.image(images[user_choice], caption="Your Choice", use_column_width=True)
            col2.image(images[computer_choice], caption="Computer's Choice", use_column_width=True, width=150 )

    # Third row: Result of the game
    st.write("Result")
    if user_choice:
        determine_winner(user_choice, computer_choice)


if __name__ == "__main__":
    main()