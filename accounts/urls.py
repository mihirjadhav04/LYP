# from django.contrib import admin
from django.urls import path, include

# from django.conf.urls.static import static

# extra part[import] for static configuration
# from django.conf import settings
# from django.conf.urls.static import static
from .views import (
    InfluencerSignUpView,
    BrandSignUpView,
    Influencers,
    InfluencerDetails,
    Brands,
    BrandDetails,
    Options,
    CommonLoginView,
    user_logout,
)

urlpatterns = [
    path("options/", Options, name="options"),
    path(
        "signup/influencer/", InfluencerSignUpView.as_view(), name="influencer_signup"
    ),
    path("signup/brand/", BrandSignUpView.as_view(), name="brand_signup"),
    path("login_page/", CommonLoginView, name="login_page"),
    path("user_logout/", user_logout, name="user_logout"),
    path("influencers/", Influencers, name="influencers"),
    path("influencer_details/<int:id>/", InfluencerDetails, name="influencer_details"),
    path("brand_details/<int:id>/", BrandDetails, name="brand_details"),
    path("brands/", Brands, name="brands"),
]
