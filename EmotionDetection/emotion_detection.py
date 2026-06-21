import requests
import json

def emotion_detector(text_to_analyze):
    # Default dictionary with None values
    default_response = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }

    # If no text provided, return default
    if not text_to_analyze or text_to_analyze.strip() == "":
        return default_response

    try:
        url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
        headers = {
            "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
        }
        myobj = {
            "raw_document": {
                "text": text_to_analyze
            }
        }

        response = requests.post(url, json=myobj, headers=headers)

        # If API fails, return default
        if response.status_code != 200:
            return default_response

        result = json.loads(response.text)

        emotions = result["emotionPredictions"][0]["emotion"]

        anger = emotions["anger"]
        disgust = emotions["disgust"]
        fear = emotions["fear"]
        joy = emotions["joy"]
        sadness = emotions["sadness"]

        scores = {
            "anger": anger,
            "disgust": disgust,
            "fear": fear,
            "joy": joy,
            "sadness": sadness
        }

        dominant = max(scores, key=scores.get)

        return {
            "anger": anger,
            "disgust": disgust,
            "fear": fear,
            "joy": joy,
            "sadness": sadness,
            "dominant_emotion": dominant
        }

    except Exception:
        # Any error → return default
        return default_response
