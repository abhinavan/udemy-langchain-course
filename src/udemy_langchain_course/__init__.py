from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.agents import create_agent
import os

from langchain_ollama import ChatOllama
from udemy_langchain_course.ecommerce_agent import search_products, apply_discount

from langchain_openai import ChatOpenAI

load_dotenv()


def askAboutCompany():
    company_description = """
    Yonex is a leading Japanese sports-equipment brand and one of the most influential names in badminton. Here are 10 lines about its role in the sport:
    
    1. Yonex was founded in Japan in 1946 and began making badminton racquets in 1957. [yonex](https://www.yonex.com/our-history)
    2. It is known worldwide for high-performance badminton racquets, strings, shuttlecocks, shoes, and apparel. [yonex](https://www.yonex.com/media/wysiwyg/Badminton_Catalog_2025_.pdf)
    3. Yonex introduced its famous ISOMETRIC square-shaped racquet head in 1992, which enlarged the sweet spot for more forgiving and powerful shots. [yonex](https://www.yonex.com/media/wysiwyg/Badminton_Catalog_2025_.pdf)
    4. Its racquet series include Astrox for power, Nanoflare for speed, and Arcsaber for control. [yonex](https://www.yonex.com/media/wysiwyg/Badminton_Catalog_2025_.pdf)
    5. Yonex has developed advanced materials and technologies, such as carbon-graphite frames and Nanoscience, to improve strength, flexibility, and shot quality. [yonex](https://www.yonex.com/media/wysiwyg/Badminton_Catalog_2025_.pdf)
    6. Since 1965, it has manufactured feather shuttlecocks known for stable flight and durability. [yonex](https://www.yonex.com/media/wysiwyg/Badminton_Catalog_2025_.pdf)
    7. Yonex shuttlecocks are used as official equipment at major Badminton World Federation events and the Olympic Games. [yonex](https://www.yonex.com/our-history)
    8. The company sponsors major tournaments, including the All England Open, one of badminton’s oldest and most prestigious championships. [yonex](https://www.yonex.com/our-history)
    9. Many top international players use Yonex equipment, helping make the brand closely associated with professional badminton. [japonity](https://japonity.com/companies/yonex-rules-the-court/)
    10. For beginners and club players, Yonex offers equipment across different budgets, making it a popular choice in badminton worldwide. [yonex](https://www.yonex.com/media/wysiwyg/Badminton_Catalog_2025_.pdf)
    """

    summary_template = """
    Given the information in the company description {company_description}, summarize the key points about Yonex's role in below format : 
    1. A short summary 
    2. Two interesting facts about the company
    3. Area of expertise
    .
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["company_description"],
        template=summary_template
    )

    llm = ChatOpenAI(model_name="gpt-5.4-nano", temperature=0.7)
    chain = summary_prompt_template | llm

    summary_response = chain.invoke(
        {"company_description": company_description})

    # print("Summary Response:")
    print(summary_response.content)


def main() -> None:
    print("Hello from udemy-langchain-course!")
    # askAboutCompany()
    tools = [search_products, apply_discount]
    # llm = ChatOpenAI(model_name="gpt-5.4-nano", temperature=0.7)
    llm = ChatOllama(model="llama3.2", temperature=0.7)
    agent = create_agent(model=llm, tools=tools)
    response = agent.invoke({"messages": [
        {"role": "user", "content": "Find me the best badminton racquet under $150 and I am a gold member"}]})
    print(response["messages"][-1].content)


if __name__ == "__main__":
    main()
