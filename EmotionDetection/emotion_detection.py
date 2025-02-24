
import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }

    r = requests.post(url, headers=headers, json=input_json)
    emotions = r.json()['emotionPredictions'][0]['emotion']
    em_values = list(emotions.values())
    max_em_value = max(em_values)
    em_keys = list(emotions.keys())
    dominant_emotion = em_keys[em_values.index(max_em_value)]
    emotions['dominant_emotion'] = dominant_emotion
    return emotions
    
        