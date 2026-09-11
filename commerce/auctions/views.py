from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Auction, Bids, Comments


def index(request):
    auctions_list = Auction.objects.all()

    return render(request, "auctions/index.html", {
        "auctions_list": auctions_list
    })

def auction(request, auction_id):
    try:
        listing = Auction.objects.get(pk=auction_id)
    except Auction.DoesNotExist:
        pass

    return render(request, "auctions/auction.html", {
        "auction": listing
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create(request):
    if request.method == "POST":
        user = request.user
        title = request.POST["title"]
        description = request.POST["description"]
        initial_value = request.POST["initial_value"]
        image = request.POST["image"]
        category = request.POST["category"]

        auction = Auction.objects.create(title=title, description=description, initial_value=initial_value, image=image, category=category, user=user)
        auction.save()
        return HttpResponseRedirect(reverse("index"))
    
    return render(request, "auctions/create.html")

def bid(request):
    if request.methoon == "POST":
        value = request.POST["value"]
        user = request.user

        Bids.objects.create(auction=auction, value=value, user=user)