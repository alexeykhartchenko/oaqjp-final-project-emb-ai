import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    myobj = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    response = requests.post(url, json=myobj, headers=header)

    # Converte a resposta JSON para um dicionário
    formatted_response = json.loads(response.text)

    # Extrai as emoções
    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    anger = emotions["anger"]
    disgust = emotions["disgust"]
    fear = emotions["fear"]
    joy = emotions["joy"]
    sadness = emotions["sadness"]

    # Descobre a emoção dominante
    dominant_emotion = max(emotions, key=emotions.get)

    # Retorna o formato solicitado
    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion
    }