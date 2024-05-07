from rasa_sdk import Rasa

rasa = Rasa(url=rasa_url, token=rasa_token)

def send_direct_message(recipient_id, text):
    rasa.send_direct_message(recipient_id, text)

def get_response(text):
    response = rasa.get_response(text)
    return response