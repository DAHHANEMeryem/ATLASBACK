import json
import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Set up the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


def analyze_intent(message):
    """
    Analyze user message to determine intent (send email, get weather, or chat)
    """
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": """You are an assistant that analyzes user messages to determine if they contain a request to:
1. Send an email (action: "send_email")
2. Get weather information (action: "get_weather")
3. Just a regular chat message (action: "chat")

For emails, extract "to", "subject", and "body" if present.
For weather, extract "location" if present.

Respond in JSON format with the following structure:
{
  "action": "send_email" | "get_weather" | "chat",
  "data": {
    // For email
    "to": "recipient email",
    "subject": "email subject",
    "body": "email content"
    // OR for weather
    "location": "city name"
  },
  "confidence": 0.0-1.0 // How confident you are in this classification
}

Only extract information that is clearly stated or can be reasonably inferred."""
                },
                {
                    "role": "user",
                    "content": message
                }
            ],
            response_format={"type": "json_object"}
        )

        return json.loads(response.choices[0].message.content)
    except Exception as e:
        print(f"Error in intent analysis: {e}")
        return {"action": "chat", "confidence": 0, "data": {}}


def generate_chat_response(message):
    """
    Generate a response for regular chat messages
    """
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating chat response: {e}")
        return "Sorry, I'm having trouble generating a response right now."
