from django.contrib import admin
from .models import Listing, User, Profile

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Listing)