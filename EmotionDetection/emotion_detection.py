import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url=url, json=data, headers=headers)
    if response.status_code == 400:
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    json_response = json.loads(response.text)
    emotions = json_response['emotionPredictions'][0]['emotion']
    dominant_emotion = ''
    max_score = 0
    for emotion in emotions:
        score = emotions[emotion]
        if score > max_score:
            max_score = score
            dominant_emotion = emotion

    emotions['dominant_emotion'] = dominant_emotion
    return emotions
    