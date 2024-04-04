import os
from dotenv import load_dotenv

class Config(object):
    def __init__(self):
        self.frontend_url = None
        self.mlarge_url = None
        self.mlarge_key = None
        self.mlarge_model = None
        self.neo4j_uri = None
        self.neo4j_user = None
        self.neo4j_password = None
        self.load_env()

    def load_env(self):
        """
        Load environment variables from .env file.
        """
        load_dotenv()
        try:
            self.frontend_url = os.getenv("INFER_GPT_FRONTEND_URL", "http://localhost:8650")
            self.mlarge_url = os.getenv("INFER_GPT_MISTRAL_LARGE_URL")
            self.mlarge_key = os.getenv("INFER_GPT_MISTRAL_LARGE_KEY")
            self.mlarge_model = os.getenv("INFER_GPT_MISTRAL_LARGE_MODEL")
            self.neo4j_uri = os.getenv("NEO4J_URI")
            self.neo4j_user = os.getenv("NEO4J_USERNAME")
            self.neo4j_password = os.getenv("NEO4J_PASSWORD")
        except FileNotFoundError:
            raise FileNotFoundError("Please provide a .env file. See the Getting Started guide on the README.md")
        except:
            raise Exception("Missing .env file property. See the Getting Started guide on the README.md")
