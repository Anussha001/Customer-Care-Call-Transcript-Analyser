import unittest
from unittest.mock import patch, Mock
from src.groq_chat_client import GroqChatClient

class TestGroqChatClient(unittest.TestCase):
    def setUp(self):
        self.api_key = "test_api_key"
        self.client = GroqChatClient(self.api_key)
        self.sample_transcript = "I love this product!"

    @patch("src.groq_chat_client.requests.post")
    def test_analyze_transcript_success(self, mock_post):
        # Mock API response JSON content
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "choices": [{
                "message": {
                    "content": '{"sentiment_analysis": {"sentiment": "positive", "summary": "Customer is happy"}}'
                }
            }]
        }
        mock_post.return_value = mock_response

        summary, sentiment = self.client.analyze_transcript(self.sample_transcript)
        self.assertEqual(summary, "Customer is happy")
        self.assertEqual(sentiment, "positive")
        mock_post.assert_called_once()

    @patch("src.groq_chat_client.requests.post")
    def test_analyze_transcript_api_error(self, mock_post):
        # Mock non-200 status code response
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.text = "Internal Server Error"
        mock_post.return_value = mock_response

        with self.assertRaises(ConnectionError):
            self.client.analyze_transcript(self.sample_transcript)

    def test_analyze_transcript_empty(self):
        with self.assertRaises(ValueError):
            self.client.analyze_transcript("")

if __name__ == "__main__":
    unittest.main()
