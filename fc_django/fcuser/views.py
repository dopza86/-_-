from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import RegisterForm, LoginForm

# Create your views here.
def index(request):
    return render(request, "index.html", {"email": request.session.get("user")})


class RegisterView(FormView):
    template_name = "register.html"
    form_class = RegisterForm
    success_url = "/"
    # 폼뷰를 사용하지 않을경우

    # if request.method =="POST"
    #     form = RegisterForm(request.POST)
    # 등을 이용하여  폼을 호출해야한다


class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = "/"

    def form_valid(self, form):
        self.request.session["user"] = form.email
        return super().form_valid(form)


def logout(request):
    if "user" in request.session:
        del request.session["user"]
    return redirect("/")
