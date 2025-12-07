from django.views.generic import DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import CustomUser
from datetime import datetime
from decimal import Decimal

# Create your views here.
class CustomUserView(DetailView):
    model = CustomUser
    template_name = 'user-profile.html'
    context_object_name = 'user'
    pk_url_kwarg = 'id'


