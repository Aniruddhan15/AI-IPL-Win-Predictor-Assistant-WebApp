"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os

import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def upload_to_gemini(path, mime_type=None):
  """Uploads the given file to Gemini.

  See https://ai.google.dev/gemini-api/docs/prompting_with_media
  """
  file = genai.upload_file(path, mime_type=mime_type)
  print(f"Uploaded file '{file.display_name}' as: {file.uri}")
  return file

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
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

# TODO Make these files available on the local file system
# You may need to update the file paths
files = [
  upload_to_gemini("Unknown File", mime_type="application/octet-stream"),
]

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "i want to create an IPL win predictor using following inputs: \n1. Team 1 name\n2. Team 2 name\n4. stadium name\n5. pitch type \n6. table ranking team 1 \n7. table ranking team 2 \n8. toss win text input\n9. decision of toss win team\n10. avg first inings score text input\n11. avg second innings score input\n12. time slot\n i want to the prediction to be accurate based on all these factors\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        files[0],
      ],
    },
    {
      "role": "user",
      "parts": [
        "i want to create an IPL win predictor using following inputs:\nTeam 1 name\nTeam 2 name\nstadium name\npitch type\ntable ranking team 1\ntable ranking team 2\ntoss win text input\ndecision of toss win team\navg first inings score text input\navg second innings score input\ntime slot\ni want to the prediction to be accurate based on all these factors",
      ],
    },
    {
      "role": "model",
      "parts": [
        "**Step 1: Data Collection**\n\n* Gather historical IPL match data including all the input features mentioned.\n* Clean and preprocess the data to remove any inconsistencies or missing values.\n\n**Step 2: Feature Engineering**\n\n* Create additional features that may be relevant for prediction, such as:\n    * Team strength based on player ratings\n    * Weather conditions\n    * Historical performance of teams in the stadium\n    * Player injuries\n\n**Step 3: Model Selection**\n\n* Choose a machine learning algorithm that is suitable for binary classification, such as:\n    * Logistic Regression\n    * Decision Tree\n    * Random Forest\n    * Support Vector Machine\n\n**Step 4: Model Training**\n\n* Split the data into training and testing sets.\n* Train the selected model using the training data.\n* Optimize model parameters using cross-validation.\n\n**Step 5: Model Evaluation**\n\n* Evaluate the performance of the trained model on the testing data.\n* Calculate metrics such as accuracy, precision, recall, and F1-score.\n* Fine-tune the model and adjust parameters as needed to improve performance.\n\n**Step 6: Deployment**\n\n* Deploy the trained model as a web service or mobile application.\n* Provide a user interface for collecting the input features.\n* Display the predicted winning team based on the model's output.\n\n**Additional Considerations for Accuracy:**\n\n* **Data Quality:** Ensure the accuracy and completeness of the historical data used for training.\n* **Feature Relevance:** Select features that are highly correlated with the outcome and avoid redundant or irrelevant features.\n* **Model Complexity:** Choose a model that is complex enough to capture the underlying relationships in the data, but not so complex that it overfits.\n* **Regular Updates:** Regularly update the model with new data to account for changes in team performance, stadium conditions, and other factors.\n\n**Disclaimer:**\n\nIt's important to note that predicting the outcome of IPL matches is a complex task and no model can guarantee 100% accuracy. The accuracy of the predictor will depend on the quality of the data, the features used, and the model's ability to generalize to unseen data.",
      ],
    },
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)