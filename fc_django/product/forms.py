from django import forms
from .models import Product


class RegisterForm(forms.Form):

    name = forms.CharField(
        error_messages={"required": "상품 이름을 입력하세요"}, max_length=256, label="상품명"
    )
    price = forms.IntegerField(
        error_messages={"required": "상품 가격을 입력하세요"}, label="상품가격",
    )
    description = forms.CharField(
        error_messages={"required": "상품 설명을 입력하세요"}, label="상품설명",
    )
    # html에서 조건문을 사용하였기에 textarea 위젯을 사용하지않음

    stock = forms.IntegerField(error_messages={"required": "재고를 입력하세요"}, label="재고",)

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        price = cleaned_data.get("price")
        description = cleaned_data.get("description")
        stock = cleaned_data.get("stock")

        if name and price and description and stock:
            product = Product(
                name=name, price=price, description=description, stock=stock
            )

            product.save()
