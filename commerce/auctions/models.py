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


    def __str__ (self):
        return f"{self.title} by {self.author}"


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
