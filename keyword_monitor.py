import requests

rasa_url = "http://localhost:5005"
rasa_token = "KELhS8MnxNaiZg_xf6c5aYQMmVr_PDZmRTet5Q-dCSw"

def monitor_keyword(reel_id, keyword, token, rasa_token):
    response = requests.get(
        f"https://graph.instagram.com/{reel_id}/comments",
        params={"fields": "text", "access_token": token}
    )
    comments = response.json()["data"]
    for comment in comments:
        if keyword in comment["text"]:
            # Send a direct message to the user who commented
            user_id = comment["from"]["id"]
            message = f"Hi! I saw your comment on my reel. Would you like to learn more about my product?"
            headers = {"Authorization": f"Bearer {rasa_token}"}
            response = requests.post(
                f"https://graph.instagram.com/v13.0/users/{user_id}/threads",
                headers=headers,
                json={"recipient_id": user_id, "message": message}
            )
            if response.status_code == 200:
                print(f"Sent direct message to user {user_id}")
            else:
                print(f"Error sending direct message: {response.text}")