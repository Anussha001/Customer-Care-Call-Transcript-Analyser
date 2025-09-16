import unittest
import os
import pandas as pd
from src.utils import save_to_csv

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.filepath = "test_call_analysis.csv"
        # Remove test file if exists before each test run
        if os.path.exists(self.filepath):
            os.remove(self.filepath)

    def tearDown(self):
        # Clean up test file after each test
        if os.path.exists(self.filepath):
            os.remove(self.filepath)

    def test_save_new_csv(self):
        transcript = "Test transcript"
        summary = "Test summary"
        sentiment = "neutral"

        save_to_csv(transcript, summary, sentiment, self.filepath)
        self.assertTrue(os.path.exists(self.filepath))

        df = pd.read_csv(self.filepath)
        self.assertEqual(df.iloc[0]["Transcript"], transcript)
        self.assertEqual(df.iloc[0]["Summary"], summary)
        self.assertEqual(df.iloc[0]["Sentiment"], sentiment)

    def test_save_append_csv(self):
        # Save first row
        save_to_csv("First transcript", "First summary", "positive", self.filepath)
        # Append second row
        save_to_csv("Second transcript", "Second summary", "negative", self.filepath)

        df = pd.read_csv(self.filepath)
        self.assertEqual(len(df), 2)
        self.assertEqual(df.iloc[1]["Transcript"], "Second transcript")
        self.assertEqual(df.iloc[1]["Sentiment"], "negative")

if __name__ == "__main__":
    unittest.main()
