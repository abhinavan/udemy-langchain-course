from dotenv import load_dotenv
from langchain.tools import tool
from langchain_core.prompts import PromptTemplate
import os

load_dotenv()


@tool
def search_weather(query: str) -> str:
    """
    Search for weather information based on the provided query.
    Args:
        query (str): The search query for weather information.
    Returns:
        str: A string containing the weather information for the given query.
    """
    print(f"Searching for weather information of city: {query}")
    # Placeholder response

    return f"Weather information for {query}: Sunny, 25°C"
