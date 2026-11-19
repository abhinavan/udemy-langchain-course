from dotenv import load_dotenv
import os

load_dotenv()


def main() -> None:
    print("Hello from udemy-langchain-course!")
    print(os.environ.get("OPENAI_API_KEY", "OPENAI_API_KEY not set"))


if __name__ == "__main__":
    main()
