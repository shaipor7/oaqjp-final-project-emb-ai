import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)
    formatted = json.loads(response.text)

    if response.status_code == 200:
        emotion = formatted["emotionPredictions"][0]["emotion"]
        output = {
            'anger': emotion["anger"],
            'disgust':emotion["disgust"],
            'fear': emotion["fear"],
            'joy': emotion["joy"],
            'sadness': emotion["sadness"],
            'dominant_emotion': max(emotion, key=emotion.get)
            }
    elif response.status_code == 400:
        output = {
            'anger': None,
            'disgust':None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
            }
    return output