from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_success')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback_form.html', {'form': form})

def feedback_success(request):
    return render(request, 'feedback/feedback_success.html')