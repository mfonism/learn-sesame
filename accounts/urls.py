from django.urls import path

from .views import LoginView, HomeView, LogoutView, GoodbyeView, AnotherView


app_name = 'accounts'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('home/', HomeView.as_view(), name='home'),
    path('another/', AnotherView.as_view(), name='another'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('goodbye/', GoodbyeView.as_view(), name='goodbye'),
]
