from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm
import random


def testimonial_view(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            if request.user.is_authenticated:
                review.user = request.user
            review.save()
            return redirect('testimonial')
    else:
        form = ReviewForm()

    all_reviews = (
        Review.objects.filter(satisfaction__gte=4)
        .order_by('first_name', 'last_name', '-created_at')
        .distinct('first_name', 'last_name')
    )

    reviews = random.sample(list(all_reviews), min(len(all_reviews), 5))

    return render(request, 'reviews/testimonial.html', {'form': form, 'reviews': reviews})
