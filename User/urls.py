from django.urls import path
from .views import CustomUserView, deposit, withdraw

urlpatterns = [
    path('<int:id>/', CustomUserView.as_view(), name='user_detail'),
    path('user/<int:id>/deposit/', deposit, name='deposit'),
    path('user/<int:id>/withdraw/', withdraw, name='withdraw'),
]