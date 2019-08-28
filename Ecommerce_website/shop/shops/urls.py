from django.urls import path
from .views import (
    HomeView,
    ProductView
)
app_name = 'shops'

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path('product/<slug>/', ProductView.as_view(), name="product"),
]
