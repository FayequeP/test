import requests

client_id = "473644571757977"
748722470778628
#2706558772844973
client_secret = "f6d4f969063d3df2344864ae1906d1c7"
#585090569efa67d45190e12474b07bcd
redirect_uri = "http://127.0.0.1:5000/authenticate"

def authenticate_instagram():
    auth_url = f"https://api.instagram.com/oauth/authorize/?client_id={client_id}&redirect_uri={redirect_uri}&scope=user_profile,user_media&response_type=code"
    print("Please go to the following URL to authenticate:")
    print(auth_url)
    code = input("Enter the authorization code: ")

    response = requests.post(
        f"https://api.instagram.com/oauth/access_token/",
        data={
            "client_id": client_id,
            "client_secret": client_secret,
            "redirect_uri": redirect_uri,
            "code": code,
            "grant_type": "authorization_code"
        }
    )

    if response.status_code == 200:
        token = response.json()["access_token"]
        return token
    else:
        print("Error authenticating with Instagram Graph API")
        return None

def get_reel_id(token):
    response = requests.get(
        "https://graph.instagram.com/me/media",
        params={"fields": "id,caption", "access_token": token}
    )
    reels = response.json()["data"]
    reel_id = reels[0]["id"]
    return reel_id