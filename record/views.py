from django.shortcuts import render
from . import models
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


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


@login_required
def make_record(request):
    if request.method == 'POST':
        record_form = forms.RecordForm(request.POST)
        if record_form.is_valid():
            new_review = record_form.save(commit=False)
            new_review.author = request.user
            new_review.save()
            return redirect('record:myrecords')
    else:
        record_form = forms.RecordForm()
    return render(request,
                  'records/record.html',
                  {'form': record_form})


def records_view(request):
    return render(request, "records/myrecords.html", )
