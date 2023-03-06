from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class User(AbstractUser):
    pass


class Listing (models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="listing_pics")
    price = models.IntegerField(default=1, validators=[MaxValueValidator(1000), MinValueValidator(0)])
    is_closed = models.BooleanField(default=False)

    # Category Field
    CLOTHING = "CL"
    SHOES = "SH"
    ACCESSORIES = "AC"
    OTHER = "OT"
    LISTING_CATEGORIES = [(CLOTHING, 'Clothing'), (SHOES, 'Shoes'), (ACCESSORIES, 'Accessories'), (OTHER, 'Other')]
    listing_categories = models.CharField(max_length=2, choices=LISTING_CATEGORIES, default=OTHER)


    def __str__ (self):
        return f"{self.title}"

class Bid(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_on = models.ForeignKey(Listing, on_delete=models.CASCADE)
    bid_amount = models.IntegerField(default=1, validators=[MaxValueValidator(1000), MinValueValidator(0)])

    def __str__(self):
        return f"{self.bidder} bid ${self.bid_amount} on {self.bid_on}"

class Profile(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} Profile"

class Watchlist(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.listing}"
