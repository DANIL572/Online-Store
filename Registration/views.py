from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from User.models import CustomUser

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_detail', id=user.id)
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration.html', {'form': form})
