from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password
from .models import Fcuser
from .forms import RegisterForm, LoginForm

# Create your views here.
def index(request):
    return render(request, "index.html", {"email": request.session.get("user")})


class RegisterView(FormView):
    template_name = "register.html"
    form_class = RegisterForm
    success_url = "/"

    def form_valid(self, form):
        fcuser = Fcuser(
            email=form.data.get("email"),  # 폼에서 데이터를 직접 받아온다
            password=make_password(form.data.get("password"), level="user"),
        )
        fcuser.save()

        # 유효성 검사를 뷰에서 직접 하고 모델에 저장까지 한다

        return super().form_valid(form)


class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = "/"

    def form_valid(self, form):
        self.request.session["user"] = form.data.get("email")  # 폼에서 데이터를 직접 받아온다
        return super().form_valid(form)


def logout(request):
    if "user" in request.session:
        del request.session["user"]
    return redirect("/")
