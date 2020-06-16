from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from fcuser.decorators import admin_required
from .models import Product
from .forms import RegisterForm
from order.forms import RegisterForm as OrderForm


# Create your views here.


class ProductList(ListView):
    model = Product
    template_name = "product.html"
    context_object_name = "product_list"


@method_decorator(admin_required, name="dispatch")
class ProductCreate(FormView):

    template_name = "register_product.html"
    form_class = RegisterForm
    success_url = "/product/"


class ProductDetail(DetailView):
    template_name = "product_detail.html"
    queryset = Product.objects.all()
    context_object_name = "product"  # 템플릿서 사용할 변수명

    """form을 전달해 주는 함수"""

    def get_context_data(self, **kwargs):  # 디테일뷰를 상속받았기에 별도의 함수로 폼을 전달해야한다
        context = super().get_context_data(**kwargs)  # 슈퍼를 통해  디테일뷰로 전달받은 데이터를 먼저만들고
        context["form"] = OrderForm(self.request)  # 여기에 내가 원하는 데이터를 추가
        # 뷰 클래스 이기 때문에 셀프안에 리퀘스트가 있다 , 폼을 생성할때 리퀘스트를 전달하게 만들어준다
        return context
