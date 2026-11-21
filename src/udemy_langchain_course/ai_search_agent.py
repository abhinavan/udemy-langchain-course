from dotenv import load_dotenv
from langchain.tools import tool
from langchain_core.prompts import PromptTemplate
import os
from tavily import TavilyClient

load_dotenv()

tavily_client = TavilyClient(api_key=os.environ.get("TAVILY_API_KEY"))


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
    if query.lower().__contains__("latest"):
        tavily_response = tavily_client.search(query)
        return tavily_response

    return f"Weather information for {query}: Sunny, 25°C"


@tool
def search_internet(query: str) -> str:
    """
    Search the internet for information based on the provided query.
    Args:
        query (str): The search query for internet information.
    Returns:
        str: A string containing the internet search results for the given query.
    """
    print(f"Searching the internet for: {query}")

    tavily_response = tavily_client.search(query)
    return tavily_response
    # Placeholder response
