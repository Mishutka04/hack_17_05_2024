import requests
from config.settings import TOKEN_TRANSFORMRS_API


headers = {"Authorization": f"Bearer {TOKEN_TRANSFORMRS_API}"}


def query_wisper(data):
    API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3" # noqa
    response = requests.post(
        API_URL,
        headers=headers,
        data=data
        )
    return response.json().get('text')


def query_sentence_transformers(payload):
    API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2" # noqa
    # payload = {
    #     "inputs": {
    #         "source_sentence": "That is a happy person",
    #         "sentences": [
    #             "That is a happy dog",
    #             "That is a very happy person",
    #             "Today is a sunny day"
    #         ]
    #     }
    # }
    response = requests.post(
        API_URL,
        headers=headers,
        json=payload
        )
    return response.json()
