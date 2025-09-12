from dotenv import load_dotenv

load_dotenv()

import os

from google import genai

from vibegen import VibeGen

# create a google gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# create a vibegen instance using the above client and specify a model
# model variants for gemini: https://ai.google.dev/gemini-api/docs/models#model-variations
vg = VibeGen(client, model="gemini-2.0-flash-lite")

# the example below tries to create a simple function for summation, without any implementations
@vg
def add_numbers(num1: int, num2: int) -> int:
    """
    This function adds two numbers 
    """
    pass

@vg
def multiply_numbers(num1: int, num2: int) -> int:
    """
    This function multiplies two numbers 
    """
    pass

print(add_numbers(3,7))
print(add_numbers(3,7231))
print(multiply_numbers(3,7))