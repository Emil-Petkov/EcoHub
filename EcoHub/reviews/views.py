from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

def testimonial_view(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            if request.user.is_authenticated:
                review.user = request.user
            review.save()
            return redirect('testimonial')
        else:
            print(form.errors)
    else:
        form = ReviewForm()

    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'reviews/testimonial.html', {'form': form, 'reviews': reviews})
