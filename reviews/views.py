from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm
from django.db import models

def review_list(request):
    reviews = Review.objects.filter(is_approved=True)
    print(reviews)
    average_rating = reviews.aggregate(models.Avg('rating'))['rating__avg']
    return render(request, 'reviews/review_list.html', {
        'reviews': reviews,
        'average_rating': average_rating or 0,
    })

@login_required
def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('review_list')
    else:
        form = ReviewForm()
    return render(request, 'reviews/submit_review.html', {'form': form})
