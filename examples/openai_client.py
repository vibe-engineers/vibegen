from dotenv import load_dotenv

load_dotenv()

import os

from openai import Client

from vibegen import VibeGen

# create an openai client
client = Client(api_key=os.getenv("OPENAI_API_KEY"))

# create a vibegen instance using the above client and specify a model
# model variants for openai: https://platform.openai.com/docs/models
vibegen = VibeGen(client, model="gpt-4.1-nano")

# the example below tries to create a simple function for summation, without any implementations
@vibegen
def add_numbers(num1: int, num2: int) -> int:
    """
    This function adds two numbers 
    """
    pass

@vibegen
def multiply_numbers(num1: int, num2: int) -> int:
    """
    This function multiplies two numbers 
    """
    pass

print(add_numbers(3,7))
print(add_numbers(3,7231))
print(multiply_numbers(3,7))