from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

from .models import CarDealer, CustomerReview
from .restapis import get_dealers_from_cf, get_dealer_reviews_from_cf, post_request

logger = logging.getLogger(__name__)


def get_dealerships(request, state="All"):
    if state == "All":
        endpoint = "/fetchDealers"
    else:
        endpoint = "/fetchDealers/" + state
    dealerships = get_dealers_from_cf(endpoint)
    return JsonResponse({"status": 200, "dealers": [d.__dict__ for d in dealerships]})


def get_dealer_details(request, dealer_id):
    if dealer_id:
        endpoint = "/fetchDealer/" + str(dealer_id)
        dealer = get_dealers_from_cf(endpoint)
        return JsonResponse({"status": 200, "dealer": dealer[0].__dict__})
    return JsonResponse({"status": 400, "message": "Bad Request"})


def get_dealer_reviews(request, dealer_id):
    if dealer_id:
        endpoint = "/fetchReviews/dealer/" + str(dealer_id)
        reviews = get_dealer_reviews_from_cf(endpoint)
        return JsonResponse({"status": 200, "reviews": [r.__dict__ for r in reviews]})
    return JsonResponse({"status": 400, "message": "Bad Request"})


def add_review(request):
    if request.user.is_anonymous is False:
        data = json.loads(request.body)
        try:
            response = post_request("/insertReview", data, dealer_id=data["dealerId"])
            return JsonResponse({"status": 200})
        except Exception:
            return JsonResponse({"status": 401, "message": "Error posting review"})
    return JsonResponse({"status": 403, "message": "Unauthorized"})


def login_request(request):
    data = json.loads(request.body)
    username = data["userName"]
    password = data["password"]
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({"userName": username, "status": "Authenticated"})
    return JsonResponse({"userName": username, "status": "Failed"})


def logout_request(request):
    logout(request)
    return JsonResponse({"userName": ""})


def registration(request):
    data = json.loads(request.body)
    username = data["userName"]
    password = data["password"]
    first_name = data["firstName"]
    last_name = data["lastName"]
    email = data["email"]
    username_exist = False
    try:
        User.objects.get(username=username)
        username_exist = True
    except Exception:
        logger.debug("{} is a new user".format(username))
    if not username_exist:
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
            email=email,
        )
        login(request, user)
        return JsonResponse({"userName": username, "status": True})
    return JsonResponse({"userName": username, "error": "Already Registered", "status": False})
