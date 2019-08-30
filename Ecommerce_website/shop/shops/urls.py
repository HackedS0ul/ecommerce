from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    HomeView,
    ProductView
)
app_name = 'shops'

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path('product/<slug>/', ProductView.as_view(), name="product"),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
