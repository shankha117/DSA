import requests
import base64
import sys

def get_token(client_id, client_secret):
    token_url = "https://us.id.planviewlogindev.net/io/v1/oauth2/token"  # Replace with actual token URL

    # Encode client_id and client_secret in base64
    credentials = f"{client_id}:{client_secret}"
    base64_code = base64.b64encode(credentials.encode()).decode()

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'Basic {base64_code}'
    }

    data = {
        'grant_type': 'client_credentials'
    }

    response = requests.post(token_url, headers=headers, data=data)

    if response.status_code != 200:
        print("Error:", response.status_code, response.text)
        sys.exit(1)

    return response.json().get('id_token')  # or access_token, depending on API

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Get OAuth2 token")
    parser.add_argument("--client_id", required=True, help="OAuth client ID")
    parser.add_argument("--client_secret", required=True, help="OAuth client secret")

    args = parser.parse_args()

    token = get_token(args.client_id, args.client_secret)
    print("Token:", token)
