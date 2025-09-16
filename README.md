# Customer-Care-Call-Transcript-Analyser

This project provides a tool to analyze customer call transcripts for sentiment and key insights using the Groq Chat API. It includes a Python implementation within a Jupyter notebook and a Streamlit web app for interactive use.

## Overview

The Customer Call Transcript Analyser processes raw customer call transcripts to deliver:

- Sentiment classification (positive, negative, neutral)
- Confidence scoring
- Identification of key phrases with sentiment context
- A concise summary of the overall sentiment in the transcript

The sentiment analysis is powered by the Groq Chat API, leveraging large language model capabilities to extract meaningful insights from customer interactions.

***

## Features

- Easy-to-use API client for interacting with Groq Chat text analysis model
- Command-line and notebook-based example demonstrating sentiment analysis
- Streamlit application for interactive transcript input and analysis
- Results saving and management via CSV file
- Downloadable CSV of all analyzed transcripts, summaries, and sentiments

***

## Technologies Used

- Python 3
- `requests` for API calls
- `pandas` for data manipulation and CSV export
- FastAPI and Uvicorn packages (already installed in notebook for environment readiness)
- Streamlit for building the web UI
- Groq Chat API for sentiment and key phrase extraction
- Pyngrok for public tunneling in Colab environments (optional)

***

## Setup and Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Anussha001/Customer-Care-Call-Transcript-Analyser.git
cd Customer-Care-Call-Transcript-Analyser
   ```

2. **Install dependencies**:

   ```bash
   pip install streamlit requests pandas fastapi uvicorn pyngrok
   ```

3. **Obtain a Groq API key** from Groq platform to use the sentiment API.

***

## Usage

### Running in Jupyter Notebook

- Load and run the `Customer_Call_Analyser.ipynb` notebook.
- Enter your Groq API key when prompted.
- Provide or modify the sample transcript to test sentiment analysis.
- View the sentiment summary and label output directly in notebook cells.

### Running the Streamlit Web App

- Run the Streamlit app locally with:

  ```bash
  streamlit run app.py
  ```

- Enter your Groq API key and paste the transcript in the UI.
- Click "Analyze" to get the sentiment and summary.
- Download the CSV file of saved analyses for record-keeping.

### Using Ngrok (optional for remote access in Colab)

- Configure ngrok with your auth token.
- Start the Streamlit app and create a public URL to share your app externally.

***

## Code Structure

- `Customer_Call_Analyser.ipynb`: Jupyter notebook containing API client example and environment setup.
- `app.py`: Streamlit app source code offering user-friendly transcript analysis interface.
- `call_analysis.csv`: Generated file storing all analyzed transcripts and results over time.

***

## Example Output

Sample transcript:

```
Hi, I was trying to book a slot yesterday but the payment failed.
```

Output summary:

```
The customer is frustrated due to a payment failure when attempting to book a slot.
```

Sentiment:

```
negative
```

***

## Contributing

Contributions are welcome! Please submit pull requests or issues to improve the project.

***

## Acknowledgements

- Groq for the Chat API providing sentiment analysis capabilities.
- Streamlit for making easy and interactive web apps for Python.

***
