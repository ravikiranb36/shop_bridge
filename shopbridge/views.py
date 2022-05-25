from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from products.models import Product


class Index(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        # GET method
        context = {"products": Product.objects.all()}

        return render(request, self.template_name, context)
