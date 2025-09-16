import os
import pandas as pd

def save_to_csv(transcript, summary, sentiment, filepath="call_analysis.csv"):
    data = {
        "Transcript": [transcript],
        "Summary": [summary],
        "Sentiment": [sentiment]
    }
    df = pd.DataFrame(data)
    if os.path.exists(filepath):
        df.to_csv(filepath, mode='a', header=False, index=False)
    else:
        df.to_csv(filepath, mode='w', header=True, index=False)
