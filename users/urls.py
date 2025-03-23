from django.urls import path

from users.views import RegisterView, LoginView, UpdateView, ProfileView, LogOutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('update/', UpdateView.as_view(), name='update'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', LogOutView.as_view(), name='logout')
]