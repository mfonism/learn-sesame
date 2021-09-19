from django import forms
from django.contrib.auth import get_user_model
from sesame.utils import get_query_string

UserModel = get_user_model()


class LoginForm(forms.Form):
    email = forms.EmailField(help_text="Email address")

    def get_sesame(self):
        print('cleaned data', self.cleaned_data)
        try:
            user = UserModel.objects.get(email=self.cleaned_data['email'])
        except UserModel.DoesNotExist:
            return ''
        qs = get_query_string(user)
        print('sesame string', qs)
        return qs


class LogoutForm(forms.Form):
    pass
