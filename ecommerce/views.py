from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def ecommerce_index(request):
    return HttpResponse("Hello, world. You're at the ecommerce index.")


def item_view(request, item_id):
    context_data = {"item_id": item_id}
    return render(request, "index.html", context=context_data)
