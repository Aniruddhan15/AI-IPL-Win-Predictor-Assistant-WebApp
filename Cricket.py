import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("google_api_key"))

generation_config = {
    "temperature": 0.35,
    "top_p": 1,
    "top_k": 0,
    "max_output_tokens": 2048,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
)

def collect_inputs():
    # Team name dropdowns
    team_names = ['CSK', 'MI', 'RCB', 'RR', 'KKR', 'SRH', 'LSG', 'GT', 'PBKS', 'DC']
    stadium_names = ["Wankhede", "Chepauk", "Chinnaswamy", "Sawai Mansingh", "Rajiv Gandhi International", 
                     "Ekana", "Narendra Modi Stadium", 
                     "Fero Shah Kotla", "Eden Gardens", "Dharamshala","Mohali"]
    pitch_types = ["Spin friendly", "Flat", "Two paced", "Slow, uneven bounce", "Green, pacy", "Equally paced"]
    time_slots = ["3 PM", "7 PM"]
    choose_to = ['bat','field']

    st.subheader("Team Selection")
    team1 = st.selectbox("Select Team 1", team_names)
    team2 = st.selectbox("Select Team 2", team_names)

    # Stadium
    st.subheader("Stadium and Pitch Conditions")
    stadium = st.selectbox("Select Stadium", stadium_names)
    pitch_type = st.selectbox("Select Pitch Type", pitch_types)


    # Table rankings
    st.subheader("Team Rankings")
    ranking_team1 = st.slider("Ranking of Team 1", 1, 10, 1)
    ranking_team2 = st.slider("Ranking of Team 2", 1, 10, 1)

    # Toss outcome
    st.subheader("Match Information")
    toss_winner = st.text_input("Toss won by (Team 1 or Team 2)")
    decision = st.selectbox("Toss decision", choose_to)

    # Average scores
    avg_first_innings_score = st.number_input("Average first innings score", min_value=0)
    avg_second_innings_score = st.number_input("Average second innings score", min_value=0)

    # Time slot
    time_slot = st.selectbox("Time Slot", time_slots)

    return (team1, team2, stadium, pitch_type, 
            ranking_team1, ranking_team2, toss_winner, decision, avg_first_innings_score, 
            avg_second_innings_score, time_slot)

def get_gemini_response(inputs):
    # Unpack inputs
    team1, team2, stadium, pitch_type, ranking_team1, ranking_team2, toss_winner, decision, avg_first_innings_score, avg_second_innings_score, time_slot = inputs
    
    # Create a prompt for the model
    prompt = (f"Predict the outcome of a cricket match with the following details:\n"
              f"Team 1: {team1}\n"
              f"Team 2: {team2}\n"
              f"Stadium: {stadium}\n"
              f"Pitch Type: {pitch_type}\n"
              f"Ranking of Team 1: {ranking_team1}\n"
              f"Ranking of Team 2: {ranking_team2}\n"
              f"Toss won by: {toss_winner}\n"
              f"Decision: {decision}\n"
              f"Average First Innings Score: {avg_first_innings_score}\n"
              f"Average Second Innings Score: {avg_second_innings_score}\n"
              f"Time Slot: {time_slot}\n"
              f"Provide a detailed prediction of the match outcome.")

    # Generate a response from the model
    response = model.generate_content(prompt)
    
    # Extract the text from the response
    return response.text if response else "Error: No response from the model."

# Set the title of the app
st.title("Cricket Win Prediction App")

# Collect inputs
inputs = collect_inputs()

submit = st.button("Predict the result!!")

# Display input summary
if submit:
    response = get_gemini_response(inputs)
    st.subheader("Here is the prediction!")
    st.write(response)
