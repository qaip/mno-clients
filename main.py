from dotenv import load_dotenv
from requests import Session

load_dotenv()


def main():
    from src.app import App
    App().run()


if __name__ == "__main__":
    main()
