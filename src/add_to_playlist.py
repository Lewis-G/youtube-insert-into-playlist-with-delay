import sys
from src.file_utils import *
from src.youtube import *

def main():
    client_secrets_file_path = "../client_secrets.json"
    
    client_data = load_client_secrets(client_secrets_file_path)
    if not client_data:
        print(f"Unable to load client data from {client_secrets_file_path}")
        sys.exit(1)
    
    refresh_token = load_refresh_token()
    
    if not refresh_token:
        credentials = run_interactive_login_flow(client_secrets_file_path)
        
        # get rid of ugly nested if blocks
        if not credentials.refresh_token:
            print("Unable to extract refresh token from interactive login")
            sys.exit(1)
        
        print("Saved refresh token")
        refresh_token = credentials.refresh_token
        save_refresh_token(refresh_token)   # Save for future use
    
    credentials = create_credentials_object_with_refresh_token(refresh_token, client_data["client_id"], client_data["client_secret"])

    if access_token_is_not_valid(credentials):
        credentials = refresh_access_token(credentials)
    
    add_to_playlist(credentials)

if __name__ == "__main__":
    main()
