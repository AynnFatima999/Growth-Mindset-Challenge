import streamlit as st
import openai
import random 


fallback_messages = [
    "Keep pushing forward! Every step you take brings you closer to success.",
    "Believe in yourself! You have the power to achieve greatness.",
    "Challenges make you stronger. Embrace them and keep growing!",
    "Success comes from perseverance. Never give up!"
]

def get_motivational_message(name, goal):
    try:
      
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a motivational coach."},
                {"role": "user", "content": f"Give a short and powerful motivational message for {name} who wants to achieve {goal}."}
            ]
        )
        return response["choices"][0]["message"]["content"]
    except:
        return random.choice(fallback_messages)


st.title("AI-Powered Daily Motivation😊") 
st.write("Get a personalized motivational message to boost your day!")

# User inputs
name = st.text_input("Enter your name:")
goal = st.text_input("What’s your goal? (e.g., Become a developer, Lose weight)")

if st.button("Get Motivation"):
    if name and goal:
        message = get_motivational_message(name, goal)
        st.success(message)
    else:
        st.warning("Please enter both your name and goal!") 


        import streamlit as st

