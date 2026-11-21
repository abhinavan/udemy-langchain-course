from dotenv import load_dotenv
from langchain.tools import tool
from langchain_core.prompts import PromptTemplate
import os
from tavily import TavilyClient

tavily_client = TavilyClient(api_key=os.environ.get("TAVILY_API_KEY"))


@tool
def search_products(query: str) -> str:
    """
    Search for products based on the provided query.
    Args:
        query (str): The search query for products.
    Returns:
        str: A string containing the product name , specs , price and buying sitefor the given query.
    """
    print(f"Searching for products related to: {query}")

    tavily_response = tavily_client.search(query)
    return tavily_response


@tool
def apply_discount(price: float, customer_loyalty: str) -> float:
    """
    Apply a discount to the given price.
    Args:
        price (float): The original price of the product.
        customer_loyalty (str): The loyalty level of the customer.
    Returns:
        float: The discounted price after applying the discount.
    """
    discount_percentage = 0
    if customer_loyalty == "gold":
        discount_percentage = 30
    elif customer_loyalty == "silver":
        discount_percentage = 20
    else:
        discount_percentage = 10

    discounted_price = price * (1 - discount_percentage / 100)
    return discounted_price
