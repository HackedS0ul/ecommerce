from django.views.generic import DetailView, ListView
from .models import Products


class HomeView(ListView):
    model = Products
    template_name = "index.html"


class ProductView(DetailView):
    model = Products
    template_name = "product-details.html"
