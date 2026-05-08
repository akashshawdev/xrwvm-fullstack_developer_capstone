"""Sentiment Analyzer Flask Microservice"""
from flask import Flask, request, jsonify
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask(__name__)


@app.route("/analyze/<text>", methods=["GET"])
def analyze_review(text):
    """Analyze sentiment of the given text"""
    result = sentiment_analyzer(text)
    label = result.get('label', None)
    score = result.get('score', None)

    if label is None:
        return jsonify({"sentiment": "neutral", "score": 0.0})

    label_map = {
        "LABEL_0": "negative",
        "LABEL_1": "neutral",
        "LABEL_2": "positive",
    }
    sentiment = label_map.get(label, "neutral")
    return jsonify({"sentiment": sentiment, "score": score})


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
