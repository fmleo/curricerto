from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views.generic.edit import FormView


class AppLoginView(LoginView):
    def get_success_url(self) -> str:
        return reverse("index")


class AppLogoutView(LogoutView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        response.headers["HX-Redirect"] = reverse("index")
        return response


class AppRegisterView(FormView):
    form_class = UserCreationForm

    template_name = "registration/register.html"

    def get_success_url(self):
        return reverse("index")
