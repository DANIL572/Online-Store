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

def deposit(request, id):
    if request.method == 'POST':
        user = get_object_or_404(CustomUser, id=id)

        try:
            amount = Decimal(request.POST.get('amount', 0))
            operation_type = request.POST.get('operation_type')

            # Проверка суммы
            if amount <= 0:
                messages.error(request, 'Сумма должна быть больше 0!')
                return redirect('user_detail', id=id)

            if operation_type == 'deposit':
                user.balance += amount
                user.save()
                messages.success(request, f'✅ Баланс пополнен на {amount} руб.!')


            else:
                messages.error(request, 'Неизвестная операция')

        except (ValueError, TypeError):
            messages.error(request, 'Ошибка: введите корректную сумму')

        return redirect('user_detail', id=user.id)

def withdraw(request,id):
    if request.method == 'POST':
        user = get_object_or_404(CustomUser, id=id)

        try:
            amount = Decimal(request.POST.get('amount', 0))
            operation_type = request.POST.get('operation_type')

            if amount <= 0:
                messages.error(request, 'Сумма должна быть больше 0!')
                return redirect('user_detail', id=id)

            if operation_type == 'withdraw':
                if user.balance >= amount:
                        user.balance -= amount
                        user.save()
                        messages.success(request, f'✅ Снято {amount} руб.!')
                else:
                    messages.error(request, f'❌ Недостаточно средств! Доступно: {user.balance} руб.')
                    return redirect('user_detail', id=id)

            else:
                messages.error(request, 'Неизвестная операция')

        except (ValueError, TypeError):
            messages.error(request, 'Ошибка: введите корректную сумму')


        return redirect('user_detail', id=user.id)
