from django.shortcuts import render, redirect
from .models import UserInfo
# Create your views here.

def submit_info(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # Save the data to the database
        UserInfo.objects.create(name=name, email=email, message=message)

        return redirect('success')

    return render(request, 'form.html')

def success(request):
    return render(request, 'success.html')