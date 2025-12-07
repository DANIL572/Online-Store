from django.urls import path
from .views import CustomUserView

urlpatterns = [
    path('<int:id>/', CustomUserView.as_view(), name='user_detail'),
]