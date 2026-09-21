from django.contrib import admin
from .models import Auction, Bids, Wishlist, Comments

# Registra os modelos no painel de administração
admin.site.register(Auction)
admin.site.register(Bids)
admin.site.register(Wishlist)
admin.site.register(Comments)