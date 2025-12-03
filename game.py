import streamlit as st
import random

st.title("🎯 Guess the Number Game")

# Initialize a secret number in session state
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(1, 100)

st.write("I'm thinking of a number between 1 and 100.")

guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Submit"):
    if guess < st.session_state.secret:
        st.warning("Too low! Try again.")
    elif guess > st.session_state.secret:
        st.warning("Too high! Try again.")
    else:
        st.success("🎉 Correct! You guessed it!")
        # Reset game
        st.session_state.secret = random.randint(1, 100)
        st.info("New number generated! Play again.")
