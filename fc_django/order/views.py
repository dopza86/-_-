from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from fcuser.decorators import login_required
from .forms import RegisterForm
from .models import Order

# Create your views here.


class OrderCreate(FormView):

    form_class = RegisterForm
    success_url = "/product/"

    def form_invalid(self, form):
        return redirect("/product/" + str(form.product))
        # form에 빠진 부분 , 즉 장석하지 않은 부분이 있을때 해당상품으로 리다이렉트 된다
        # 템플릿 이름을 지정하지않아 에러가 발생했을때 처리하는 함수

    # FormView 안에서도 리퀘스트를 전달하도록 만들어야 한다
    def get_form_kwargs(self, **kwargs):  # 폼을 생성할때 어떤 인자값을 전달하여 만들지 결정하는 함수
        kw = super().get_form_kwargs(**kwargs)  # 기존에 있는 함수 호출,kw 라는 변수안에 폼뷰가 생성하는 인자값들 입력
        kw.update({"request": self.request})  # 윗줄 kw 에 request라는 인자값 추가
        return kw  # 리턴해주면 기존에 자동으로 생성되는 인자값에 request라는 인자값도 함께 추가하여 폼을 만들겠다


@method_decorator(login_required, name="dispatch")  # dispatch 란 함수에 대해 login_required 데코레이터 적용
class OrderList(ListView):
    # model = Order #이렇게 하면 모든 유저의 주문정보가 표시된다 get_queryset 함수를 오버라이딩 하여 쿼리셋을 이용한다
    template_name = "order_list.html"
    context_object_name = "order_list"

    def get_queryset(self, **kwargs):
        queryset = Order.objects.filter(fcuser__email=self.request.session.get("user"))
        return queryset
