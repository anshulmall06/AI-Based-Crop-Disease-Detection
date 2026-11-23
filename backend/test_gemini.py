
import os
from google import genai
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found. Please check your .env file."
    )

# Initialize Gemini client
client = genai.Client(api_key=api_key)

print("Testing Gemini API...\n")

try:
    # Generate content using Gemini
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=(
            "Explain Tomato Early Blight, its symptoms and "
            "prevention methods in simple English."
        )
    )

    # Display response
    print("=" * 50)
    print("GEMINI RESPONSE")
    print("=" * 50)

    if response.text:
        print(response.text)
    else:
        print("Gemini returned an empty response.")

except Exception as e:
    print("\nGemini API Error:")
    print(e)
