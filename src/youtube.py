import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import google.auth.transport.requests
from google.oauth2.credentials import Credentials

def create_credentials_object_with_refresh_token(refresh_token, client_id, client_secret):
    credentials = Credentials.from_authorized_user_info({
        "refresh_token": refresh_token,
        "client_id": client_id,
        "client_secret": client_secret,
        "token_uri": "https://oauth2.googleapis.com/token"
    })
    return credentials

def run_interactive_login_flow(client_secrets_file_path:str):
    # Define the OAuth scope
    scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
    
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file_path, scopes)
        
    credentials = flow.run_local_server()
    return credentials

def access_token_is_not_valid(credentials:Credentials):
    return credentials.expired

def refresh_access_token(credentials:Credentials):
    request = google.auth.transport.requests.Request()
    credentials.refresh(request)
    return credentials
    
def add_to_playlist(credentials:Credentials):
    # Build the YouTube API client
    youtube = googleapiclient.discovery.build(
        "youtube", "v3", credentials=credentials)

    # Make a request to the API
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        mine=True
    )
    response = request.execute()

    print(response)