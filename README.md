# AI-IPL-Win-Predictor-Assistant-WebApp

# Complete End to End Grandeur IPL Predictor app

# Disclaimer: 
This app is purely for cricket enthusiats, technologists who love to integrate tech into the domain of cricket and sports. <br/> This app helps to provide key insights about the match.<br/> Hence utilise the freedom of prompt/intention and individual with approporiate terms,usage of language.
# Overview
The Cricket Predictor App utilizes the Gemini Pro pre-trained model to predict cricket match outcomes based on various input factors such as team names, stadium conditions, pitch types, and more.<br/> This app provides cricket enthusiasts and analysts with accurate match insights, enhancing their understanding and enjoyment of the game.

# Objective:
The primary objective of the Cricket Predictor App is to provide users with precise and insightful predictions of cricket match outcomes.<br/> By leveraging advanced AI models and considering various factors that influence the game, the app aims to assist cricket fans, analysts, and enthusiasts in making informed predictions and analyses.

# Proposed Solution
To achieve the objective, the app integrates the Gemini Pro pre-trained model through a streamlined process: <br/>
User Interaction: Users interact with an intuitive UI to enter match details such as team names, stadium, pitch conditions, and other relevant factors.<br/>
Data Collection: The app securely collects user inputs and transmits them to the backend using a Google API key.<br/>
API Integration: User inputs are forwarded to the Gemini Pro model via an API call.<br/>
Model Processing: The Gemini Pro pre-trained model processes the inputs and generates predictions.<br/>
Result Display: The results are returned to the frontend, where they are formatted and displayed to the user.<br/>

# Features
User Input Collection: Intuitive interface for entering match details.<br/>
Prediction Generation: Uses the Gemini Pro model to generate detailed match predictions.<br/>
Secure Data Handling: Ensures data privacy and security.<br/>
Customizable Settings: Allows configuration of prediction parameters.<br/>
Performance Optimization: Delivers rapid and reliable predictions.<br/>
Deployment Ready: Scalable and accessible from any device.<br/>

# **Screenshots of the web app**
**Sample 1**

![Screenshot 2024-07-08 135428](https://github.com/Aniruddhan15/AI-IPL-Win-Predictor-Assistant-WebApp/assets/137152187/cbbf0c8f-40cc-40d1-9d39-fea2dc57b7eb)

![Screenshot 2024-07-08 135340](https://github.com/Aniruddhan15/AI-IPL-Win-Predictor-Assistant-WebApp/assets/137152187/c5cbfbd6-757f-47f7-964b-d7ee2979f9ea)

![Screenshot 2024-07-08 135428](https://github.com/Aniruddhan15/AI-IPL-Win-Predictor-Assistant-WebApp/assets/137152187/ce29ca8c-461f-40fa-bbff-9c4d0ce6394c)


# **Web App Deploy**: <br/>Streamlit community cloud
Public Link: https://ai-ipl-win-predictor-assistant-webapp-dgd9dapr4jga9wrryjpkxg.streamlit.app/

# Step by Step Set-Up Instructions

# 0. Requirements
Python 3.7+ <br/>
Streamlit <br/>
Google Generative AI library <br/>
dotenv <br/>

Software Requirements: <br/>
VsCode <br/>
AI Studio Account <br/>
Streamlit Community Account for Deployment

# 1.**Clone the repository:** 
# AI Cricket Assisstant App

## Clone the Repository

To clone the repository, use the following command:

<pre>
<code id="clone-code-aniruddhan">
git clone (https://github.com/Aniruddhan15/AI-IPL-Win-Predictor-Assistant-WebApp.git)
</code>
</pre>


# 2.**Navigate to the project directory:** 
cd ai-Cricket-Assisstant-app

# 3.**Install the required libraries:** <br/>
<pre>
<code id="install-code">
pip install -r requirements.txt
</code>
</pre>

# 4.**Set up your Google API Key and other environment variables as needed.** <br/>
Obtain an API key from makersuite google for gemini pro vision api key: <br/>
Visit the AI Studio website (https://aistudio.google.com/app/apikey) and sign up in order to obtain the API key access. <br/>
Follow the instructions provided by AI studio Google to obtain an API key.<br/>
Copy the API key as you will need it in the next step.<br/>
Add your API key to the app.py file:<br/>
Open the Cricket.py file in a text editor.<br/>
Locate the line that says genai.api_key = 'YOUR_API_KEY'.<br/>
Replace 'YOUR_API_KEY' with the API key you obtained from AIStudio.<br/>
Save the Cricket.py file.

# Alternative/ Best option:
Create a ".env" file to your environment and add your api key as google_api_key="(Put Your api key, please dont forget to include as a string)" <br/>
use the below code: 
<pre>
<code id="Loading-api">
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("google_api_key"))
</code>
</pre>


# 5.**Run the application:** <br/>
python Cricket.py

 # 6.**Access the app** 
To start Streamlit web browser, use the following command:
<pre>
<code id="start-streamlit">
streamlit run Cricket.py
</code>
</pre>
You can view your web browser at (http://localhost:5000) (or http://127.0.0.1:5000) or at a recommended browser link in the comman prompt console. <br/>
Register your desired meal picture and a prompt about it start receiving personalized meal plans and tracking your nutrition.

# **Contributing** 
We welcome contributions to enhance the AI Nutrition App.<br/> please fork the repository, create a new branch for your feature or bug fix, and submit a pull request.<br/> Make sure to follow our coding guidelines and include appropriate tests.

# **Contributing Guidelines**
Fork the repository.Create a new branch.
<pre>
<code id="Fork the repository">
git checkout -b feature-branch
</code>
</pre>

**Make your changes.**

**Commit your changes.**
<pre>
<code id="Commit the changes">
git commit -am 'Add new feature'
</code>
</pre>

**Push to the branch** 
<pre>
<code id="Push to origin">
git push origin feature-branch
</code>
</pre>

**Create a new Pull Request.**

# Host the Application
Choose a hosting platform (e.g., Heroku, AWS, Google Cloud Platform) and deploy your application following platform-specific instructions.<br/>
I used Streamlit Deploy and hosting services

# **License**
Apache License <br/>
Version 2.0, January 2004

# Contact
N Aniruddhan - aniruddhan26@gmail.com
