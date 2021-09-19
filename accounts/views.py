from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import LoginForm, LogoutForm


class LoginView(FormView):
    form_class = LoginForm
    success_url = reverse_lazy('accounts:home')
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        self.success_url = self.success_url + form.get_sesame()
        return super().form_valid(form)


class HomeView(TemplateView):
    template_name = 'accounts/home.html'


class LogoutView(FormView):
    form_class = LogoutForm
    success_url = reverse_lazy('accounts:goodbye')
    template_name = 'accounts/logout.html'

    def form_valid(self, form):
        logout(self.request)
        return super().form_valid(form)


class GoodbyeView(TemplateView):
    template_name = 'accounts/goodbye.html'


class AnotherView(TemplateView):
    template_name = 'accounts/another.html'
