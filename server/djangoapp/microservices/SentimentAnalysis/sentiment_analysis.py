"""Sentiment Analysis using VADER"""
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon', quiet=True)


def sentiment_analyzer(text):
    """Return sentiment label and score for given text"""
    try:
        analyzer = SentimentIntensityAnalyzer()
        scores = analyzer.polarity_scores(text)
        compound = scores['compound']

        if compound >= 0.05:
            return {"label": "LABEL_2", "score": compound}  # positive
        elif compound <= -0.05:
            return {"label": "LABEL_0", "score": compound}  # negative
        else:
            return {"label": "LABEL_1", "score": compound}  # neutral
    except Exception as err:
        print("Error in sentiment analysis:", str(err))
        return {"label": "LABEL_1", "score": 0.0}
