import json
import os
from dotenv import load_dotenv

def load_client_secrets(client_secrets_file_path:str):
    with open(client_secrets_file_path, "r") as file:
            client_data = json.load(file)["installed"]
            return client_data

def load_refresh_token():
    # Load environment variables from .env file
    load_dotenv()
    return os.getenv("REFRESH_TOKEN")

def save_refresh_token(refresh_token:str):
    with open(".env", "w") as env_file:
        env_file.write(f"REFRESH_TOKEN={refresh_token}\n")