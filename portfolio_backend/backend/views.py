from django.shortcuts import redirect, render

from .models import *

# Create your views here.

def home(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print(name, email, message)
        reviewForm.objects.create(name=name, email=email, message=message)
        return redirect('thankyou')

    return render(request, 'index.html')

def thankyou(request):

    return render(request, 'thankyou.html')
