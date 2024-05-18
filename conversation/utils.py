import requests
import stable_whisper
from gradio_client import Client
from config.settings import TOKEN_TRANSFORMRS_API


headers = {"Authorization": f"Bearer {TOKEN_TRANSFORMRS_API}"}


def query_wisper(data):
    API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3" # noqa
    response = requests.post(
        API_URL,
        headers=headers,
        data=data
        )
    re = response.json().get('text')
    print(re)
    return re


# def query_wisper(data):
#     whisper_model = stable_whisper.load_model(
#     'large-v3',
#     download_root="/media/robot/files/analyzer_offic_ negotiations/ml_models")  # noqa
#     result = whisper_model.transcribe(data)
#     # print(result.text)
#     # result.save_as_json("data.json")
#     return result.text



def query_sentence_transformers(payload):
    API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2" # noqa
    response = requests.post(
        API_URL,
        headers=headers,
        json=payload
        )
    return response.json()


def query_predict_nlp(input_message):
    
    client = Client("https://qwen-qwen1-5-72b-chat.hf.space/--replicas/3kh1x/")
    result = client.predict(
        input_message,
        [["None", "None"]],
        "None",
        api_name="/model_chat"
    )
    
    return result[1][1][1]

