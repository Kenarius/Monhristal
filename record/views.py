from django.shortcuts import render
from . import models


# Create your views here.
def main_view(request):
    return render(request, 'records/main.html')


def review_view(request):
    reviews = models.Review.objects.all()
    return render(request, "records/reviews.html",
                  {"reviews": reviews})
