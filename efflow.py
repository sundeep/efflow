"""
Simple query script, basic fuckery
"""
import requests

API_URL = "https://api-inference.huggingface.co/models/microsoft/prophetnet-large-uncased-squad-qg"
headers = {"Authorization": "Bearer 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"}


def query(payload):
    """issue the query to huggingface"""
    response = requests.post(API_URL, headers=headers, json=payload, timeout=10)
    return response.json()


txt = (
    "I have a VW gti that needs to be sold.",
    "To get it ready for sale, I need to make sure it works and looks good. ",
    "It is currently not starting, and looks pretty shitty.",
    "I don't know how much it would cost to get it ready for sale",
)
inny = {"inputs": txt}
output = query(inny)

print(output)
