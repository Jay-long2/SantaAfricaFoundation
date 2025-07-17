from django.shortcuts import render, redirect
from .forms import NewsletterForm , ContactForm
from .models import NewsletterSubscriber

# Create your views here
def home(request):
    form = NewsletterForm()

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # or render with a success message

    return render(request, 'core/home.html', {'form': form})


def about(request):
    return render(request, 'core/about.html')

def resources(request):
    return render(request, 'core/resources.html')

def contact(request):
    form = ContactForm()
    success = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True

    return render(request, 'core/contact.html', {'form': form, 'success': success,})





def contact_details(request):
    return render(request, 'core/contact_details.html',{
        'paystack_public_key': settings.PAYSTACK_TEST_KEY
    })

def terms(request):
    return render(request, 'core/terms.html')

def privacy(request):
    return render(request, 'core/privacy.html')

from django.conf import settings

def donate(request):
    context = {
        'paystack_test_key': settings.PAYSTACK_TEST_KEY
    }
    return render(request, 'core/donate.html', context)
