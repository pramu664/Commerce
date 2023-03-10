from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("<int:pk>", views.listing_detail, name="listing_detail"),

    path("bid", views.bid, name="bid"),
    path("bid_options", views.bid_options, name="bid_options"),

    path("watchlist", views.watchlist_view, name="watchlist"),
    path("add_to_watchlist", views.add_to_watchlist, name="add_to_watchlist"),
    path("remove_from_watchlist", views.remove_from_watchlist, name="remove_from_watchlist"),

    path("category/<str:name>", views.show_category, name="category"),

    path("profile", views.profile, name="profile"),

    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]

