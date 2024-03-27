import streamlit as st
import random

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

    # User choice
    user_choice = st.radio("Choose your move:", options=['rock', 'paper', 'scissors'])

    # Computer choice
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    # Determine winner
    result = determine_winner(user_choice, computer_choice)

    # Display choices and result
    st.write(f"You chose: {user_choice}")
    st.write(f"Computer chose: {computer_choice}")
    st.write(f"Result: {result}")

if __name__ == "__main__":
    main()
