import requests
import os
from dotenv import load_dotenv
from .models import CarDealer, CustomerReview

load_dotenv()

backend_url = os.getenv("backend_url", default="http://localhost:3030")
sentiment_analyzer_url = os.getenv("sentiment_analyzer_url", default="http://localhost:5050/")


def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params += key + "=" + value + "&"
    request_url = backend_url + endpoint + "?" + params
    print("GET from {} ".format(request_url))
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as e:
        print("Network exception occurred: " + str(e))
        return None


def post_request(endpoint, json_payload, **kwargs):
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params += key + "=" + str(value) + "&"
    request_url = backend_url + endpoint + "?" + params
    print("POST to {} ".format(request_url))
    try:
        response = requests.post(request_url, json=json_payload)
        return response.json()
    except Exception as e:
        print("Network exception occurred: " + str(e))
        return None


def get_dealers_from_cf(endpoint, **kwargs):
    results = []
    json_result = get_request(endpoint, **kwargs)
    if json_result:
        dealers = json_result
        if isinstance(json_result, dict):
            dealers = json_result.get("dealers", [])
        for dealer in dealers:
            dealer_obj = CarDealer(
                address=dealer.get("address", ""),
                city=dealer.get("city", ""),
                full_name=dealer.get("full_name", ""),
                id=dealer.get("id", 0),
                lat=dealer.get("lat", 0),
                long=dealer.get("long", 0),
                short_name=dealer.get("short_name", ""),
                st=dealer.get("st", ""),
                zip=dealer.get("zip", ""),
            )
            results.append(dealer_obj)
    return results


def get_dealer_reviews_from_cf(endpoint, **kwargs):
    results = []
    json_result = get_request(endpoint, **kwargs)
    if json_result:
        reviews = json_result
        if isinstance(json_result, dict):
            reviews = json_result.get("reviews", [])
        for review in reviews:
            review_obj = CustomerReview(
                id=review.get("id", 0),
                name=review.get("name", ""),
                dealership=review.get("dealership", 0),
                review=review.get("review", ""),
                purchase=review.get("purchase", False),
                purchase_date=review.get("purchase_date", ""),
                car_make=review.get("car_make", ""),
                car_model=review.get("car_model", ""),
                car_year=review.get("car_year", ""),
            )
            review_obj.sentiment = analyze_review_sentiments(review_obj.review)
            results.append(review_obj)
    return results


def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "analyze/" + text
    try:
        response = requests.get(request_url)
        return response.json().get("sentiment", "neutral")
    except Exception as e:
        print("Sentiment analyzer error: " + str(e))
        return "neutral"
