from django.shortcuts import render
from . import models
from . import forms
from django.contrib.auth.models import User
from .forms import ReviewForm
from django.shortcuts import redirect


# Create your views here.
def main_view(request):
    return render(request, 'records/main.html')


def review_view(request):
    reviews = models.Review.objects.all()
    return render(request, "records/reviews.html",
                  {"reviews": reviews})


def write_review(request):
    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.author = User.objects.first()
            new_review.save()
            return redirect('record:review')
    else:
        review_form = forms.ReviewForm()
    return render(request,
                  'records/write.html',
                  {'form': review_form})
