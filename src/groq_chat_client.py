import requests
import json

class GroqChatClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def analyze_transcript(self, transcript: str, model: str = "openai/gpt-oss-20b"):
        if not transcript.strip():
            raise ValueError("Transcript is empty.")

        system_content = (
            "You are a data analysis API that performs sentiment analysis on text.\n"
            "Respond only with JSON using this format:\n"
            "{\n"
            ' "sentiment_analysis": {\n'
            '   "sentiment": "positive|negative|neutral",\n'
            '   "confidence_score": 0.95,\n'
            '   "key_phrases": [\n'
            '       {\n'
            '         "phrase": "detected key phrase",\n'
            '         "sentiment": "positive|negative|neutral"\n'
            '       }\n'
            '    ],\n'
            '   "summary": "One sentence summary of the overall sentiment"\n'
            '  }\n'
            '}'
        )

        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_content},
                {"role": "user", "content": f"Analyze the sentiment of this customer review: '{transcript}'"}
            ],
            "response_format": {"type": "json_object"}
        }

        response = requests.post(self.api_url, json=payload, headers=self.headers)
        if response.status_code != 200:
            raise ConnectionError(f"API Error {response.status_code}: {response.text}")

        response_json = response.json()
        message_content = response_json.get("choices", [{}])[0].get("message", {}).get("content", "{}")
        result = json.loads(message_content)

        sentiment_analysis = result.get("sentiment_analysis", {})
        summary = sentiment_analysis.get("summary", "")
        sentiment = sentiment_analysis.get("sentiment", "")

        return summary, sentiment
