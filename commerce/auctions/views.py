from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required


from .models import User, Listing, Watchlist, Bid
from .forms import ListingForm, BiddingForm

@login_required
def index(request):
    listings = {"listings": Listing.objects.all()}
    return render(request, "auctions/index.html", listings)


@login_required
def bid(request):
    if request.method == "POST":
        bid_amount = request.POST["bid"]
        listing_id = request.POST["id"]
        listing = Listing.objects.get(id=listing_id)
        current_listing_price = listing.price
        
        if int(bid_amount) < int(current_listing_price):
            messages.warning(request, f"Bid must be greater than current listing price")
            return HttpResponseRedirect(reverse("listing_detail", args=(listing_id,)))

        if not request.user.id == listing.author.id:
            listing.price = bid_amount
            listing.save()
        
            bid = Bid.objects.create(bidder=request.user, bid_on=listing, bid_amount=bid_amount)
            messages.success(request, f"Successfully bid ${bid_amount} on {listing}")
            return HttpResponseRedirect(reverse("listing_detail", args=(listing_id,)))
        else:
            messages.warning(request, f"You can't bid on your own listings")
            return HttpResponseRedirect(reverse("listing_detail", args=(listing_id,)))


    form = BiddingForm()
    return render(request, "auctions/bid.html", {"form": form})

@login_required
def bid_options(request):
    option = request.POST["option"]

    # Convert option to boolean values
    if option == "True":
        option = True
    elif option == "False":
        option == False

    # Get the listing that user working on
    listing_id = request.POST["id"]
    listing = Listing.objects.get(id=listing_id)

    # Handle Open listing and Close listing
    if option == True:# Closing
        listing.is_closed = option
        listing.save()
        messages.success(request, f"{listing} now closed")
        return HttpResponseRedirect(reverse("listing_detail", args=(listing_id,)))
    else:# Opening
        listing.is_closed = option
        listing.save()
        messages.success(request, f"{listing} now opened")
        return HttpResponseRedirect(reverse("listing_detail", args=(listing_id,)))


@login_required
def watchlist_view(request):
    watchlist = Watchlist.objects.all().filter(customer=request.user)
    return render (request, "auctions/watchlist.html", {"watchlist": watchlist})

@login_required
def add_to_watchlist(request):
    if request.POST:
        listing_id = request.POST["id"]
        listing = Listing.objects.filter(id=listing_id).first()
        if not request.user.id == listing.author.id:
            if not Watchlist.objects.filter(listing=listing):
                watchlist = Watchlist.objects.create(customer=request.user, listing=listing)
                messages.success(request, f"{watchlist} added successfully.")
                return HttpResponseRedirect(reverse("listing_detail", args=(listing_id,)))
            else:
                messages.warning(request ,f"Already {listing} in your wishlist")
                return HttpResponseRedirect(reverse("listing_detail", args=(listing_id,)))
        else:
            messages.warning(request ,f"You can't add your own listings for wishlist. Try adding someone else listing.")
            return HttpResponseRedirect(reverse("listing_detail", args=(listing_id,)))

@login_required
def remove_from_watchlist(request):
    watchlist_id = request.POST["id"]
    watchlist_item = Watchlist.objects.get(id=watchlist_id)
    watchlist_item.delete()
    messages.success(request, f"{watchlist_item} removed successfully.")
    return HttpResponseRedirect(reverse("watchlist"))

@login_required
def create_listing(request):
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("author")
            messages.success(request, f"Listing created by {username}")
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.warning(request, f"Price must be in between $1 and $1000")

    user = request.user
    data = {"author_id": user.id, "author": user} 
    form = ListingForm(initial=data)
    return render (request, "auctions/create_listing.html", {"form": form}) 


@login_required
def listing_detail(request, **kwargs):
    pk = kwargs.get('pk')
    try:
        listing = Listing.objects.get(pk=pk)
    except ObjectDoesNotExist:
        messages.warning(request, f"does not exist!")
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/listing.html", {"listing": listing})



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
