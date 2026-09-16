from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import User, Auction, Bids, Comments, Wishlist


def index(request):
    auctions_list = Auction.objects.all()
    user = request.user
    if request.user.is_authenticated:
        wishes_number = Wishlist.objects.filter(user=user).count()
    else:
        wishes_number = None

    return render(request, "auctions/index.html", {
        "auctions_list": auctions_list,
        "wishes_number": wishes_number
    })

def auction(request, auction_id):
    user = request.user
    auction = get_object_or_404(Auction, pk=auction_id)
    antigo_bid = Bids.objects.filter(auction_id=auction_id).order_by("value").last()
    wishlist = Wishlist.objects.filter(user=user,auction=auction).exists()
    bids = Bids.objects.filter(auction_id=auction_id).count
    wishes_number = Wishlist.objects.filter(user=user).count()

    if antigo_bid.user == user:
        your_bid = antigo_bid
    if antigo_bid.user != user:
        have_bid = Bids.objects.filter(auction_id=auction_id, user=user).exists()
    else:
        have_bid = None

    try:
        listing = Auction.objects.get(pk=auction_id)
    except Auction.DoesNotExist:
        pass

    return render(request, "auctions/auction.html", {
        "auction": listing,
        "auction_id": auction_id,
        "antigo_bid": antigo_bid,
        "wishlist": wishlist,
        "bids": bids,
        "your_bid": your_bid,
        "have_bid": have_bid,
        "wishes_number": wishes_number
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

def bid(request, auction_id):
    if request.method == "POST":
        value = float(request.POST["value"])
        user = request.user

        antigo_bid = Bids.objects.filter(auction_id=auction_id).order_by("value").last()

        auction = get_object_or_404(Auction, pk=auction_id)

        if antigo_bid is None or value > antigo_bid.value:
            antigo_bid = Bids.objects.create(auction=auction, value=value, user=user)

            return HttpResponseRedirect(reverse("auction", kwargs={"auction_id": auction_id}))
            
        else:
            return render (request, "auctions/auction.html", {
                    "auction_id": auction_id,
                    "error": "Bid needs to be bigger than the actual bid",
                })
    return render(request, "auctions/auction.html", {
        "auction_id": auction_id
    })

def wishlist(request, auction_id):
    if request.method == "POST":
        user = request.user
        auction = get_object_or_404(Auction, pk=auction_id)
        wishes_number = Wishlist.objects.filter(user=user).count()
        
        Wishlist.objects.create(user=user, auction=auction)

        return HttpResponseRedirect(reverse("auction", kwargs={"auction_id": auction_id}))
    return render (request, "auctions/auction.html", {
        "auction_id": auction_id,
        "wishes_number": wishes_number
    })

def deletewishlist(request, auction_id):
    if request.method == "POST":
        user = request.user
        auction = get_object_or_404(Auction, pk=auction_id)

        Wishlist.objects.filter(user=user, auction=auction).delete()
    
        return HttpResponseRedirect(reverse("auction", kwargs={"auction_id": auction_id}))
    
def showwishlist(request):
    user = request.user
    wishes_number = Wishlist.objects.filter(user=user).count()
    auctions_list = Auction.objects.filter(wishlist__user=request.user)

    return render(request, "auctions/wishlist.html", {
        "auctions_list": auctions_list,
        "wishes_number": wishes_number
    })