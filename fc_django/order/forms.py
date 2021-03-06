from django import forms
from .models import Order
from product.models import Product  # 모델에서 외래키로 연결이 되있기 때문에 모델에서 가져온다
from fcuser.models import Fcuser  # 모델에서 외래키로 연결이 되있기 때문에 모델에서 가져온다
from django.db import transaction


class RegisterForm(forms.Form):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    # 사용자 정보를 가져오기 위해서는 세션에 접근해야 하기 때문에 생성자 함수를 만든다
    # 폼을 생성하는 부분을 상품상세보기 뷰에 있다
    quantity = forms.IntegerField(error_messages={"required": "수량 을 입력하세요"}, label="수량")

    product = forms.IntegerField(
        error_messages={"required": "상품 설명을 입력하세요"}, widget=forms.HiddenInput, label="상품설명",
    )

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get("quantity")
        product = cleaned_data.get("product")
        fcuser = self.request.session.get("user")  # 세션에서 유저를 가져온다 ->email->로그인된 놈 을 가져온다

        if not (quantity and product and fcuser):
            # self.product = product  # 폼뷰에서 사용된다
            self.add_error("quantity", "값이 없습니다")
            self.add_error("product", "값이 없습니다")

        # print(self.request.session) #상품에서 주문하기 눌렀을때 세션생성을 콘솔에서 확인가능
