import requests
import json
 #function to to analyze the emotion
def emotion_detector(text_to_analyze):
     url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
     headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
     myobj= { "raw_document": { "text": text_to_analyze } }
     response = requests.post(url, json = myobj, headers=headers)

    # Convert API response
     result = json.loads(response.text)

    # Extract emotion scores
     emotions = result["emotionPredictions"][0]["emotion"]

     anger = emotions["anger"]
     disgust = emotions["disgust"]
     fear = emotions["fear"]
     joy = emotions["joy"]
     sadness = emotions["sadness"]

    # Find dominant emotion
     scores = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness
     }
     dominant = max(scores, key=scores.get)

    # Return final dictionary
     return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant
     }

