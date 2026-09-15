from django.contrib import admin
from .models import Auction, Bids, Wishlist

# Registra os modelos no painel de administração
admin.site.register(Auction)
admin.site.register(Bids)
admin.site.register(Wishlist)