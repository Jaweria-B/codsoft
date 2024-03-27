import streamlit as st
import random

# Dictionary containing image paths for each choice
images = {
    "rock": "./assets/rock.png",      # Replace with actual path
    "paper": "./assets/paper.png",     # Replace with actual path
    "scissors": "./assets/scissors.png"   # Replace with actual path
}

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def main():
    st.title("Rock-Paper-Scissors Game")

    # First row: User's choice and computer's choice
    col1, col2 = st.columns(2)
    user_choice = col1.radio("Your Choice:", ["rock", "paper", "scissors"], key="user_choice")
    if user_choice:
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        col2.write(f"Computer's Choice: {computer_choice.title()}")

    # Second row: Image cards for user's and computer's choices
    st.write("")
    col1, col2 = st.columns(2)
    if user_choice:
        col1.image(images[user_choice], caption="Your Choice", use_column_width=True)
        col2.image(images[computer_choice], caption="Computer's Choice", use_column_width=True)

    # Third row: Result of the game
    st.write("")
    if user_choice:
        result = determine_winner(user_choice, computer_choice)
        st.write(f"Result: {result}")

if __name__ == "__main__":
    main()