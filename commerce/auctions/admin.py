from django.contrib import admin
from .models import Listing, User, Profile, Watchlist

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Listing)
admin.site.register(Watchlist)