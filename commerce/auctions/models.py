from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Auction(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    initial_value = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=True)
    image = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auction")
    watchlist = models.ManyToManyField(User, blank=True, related_name="watchlist")
    closed = models.BooleanField(blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    winner = models.ForeignKey(User, blank=True, null=True, related_name="winner", on_delete=models.CASCADE)

class Bids(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="bids")
    value = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")

class Comments(models.Model):
    message = models.TextField(blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="comments")

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishlist")
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="wishlist")
    