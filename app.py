from flask import Flask, request, jsonify, redirect
from instagram_auth import client_id, redirect_uri, client_secret
from keyword_monitor import monitor_keyword
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/authenticate", methods=["GET"])
def authenticate():
    auth_url = f"https://api.instagram.com/oauth/authorize/?client_id={client_id}&redirect_uri={redirect_uri}&scope=user_profile,user_media&response_type=code"
    return redirect(auth_url)

@app.route("/callback", methods=["GET"])
def callback():
    code = request.args.get("code")
    token_url = f"https://api.instagram.com/oauth/access_token/"
    response = request.post(
        token_url,
        data={
            "client_id": client_id,
            "client_secret": client_secret,
            "redirect_uri": redirect_uri,
            "code": code,
            "grant_type": "authorization_code"
        }
    )
    token = response.json()["access_token"]
    return jsonify({"token": token})

@app.route("/monitor", methods=["POST"])
def monitor():
    reel_id = request.json["reel_id"]
    keyword = request.json["keyword"]
    token = request.json["token"]  # Get the token from the request
    monitor_keyword(reel_id, keyword, token)  # Pass the token to the monitor_keyword function
    return jsonify({"message": "Keyword monitoring started"})

if __name__ == "__main__":
    app.run(debug=True)