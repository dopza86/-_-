from django.db import models

# Create your models here.


class Fcuser(models.Model):
    """Custom User Model """

    LEVEL_1 = "user"
    LEVEL_2 = "admin"

    LEVEL_CHOICE = (
        (LEVEL_1, "user"),
        (LEVEL_2, "admin"),
    )

    email = models.EmailField(verbose_name="이메일")
    password = models.CharField(max_length=128, verbose_name="비밀번호")
    level = models.CharField(choices=LEVEL_CHOICE, max_length=32, verbose_name="레벨")  # , null=True)
    register_date = models.DateTimeField(auto_now_add=True, verbose_name="등록날짜")

    def __str__(self):
        return self.email

    class Meta:
        db_table = "fastcampus_fcuser"
        verbose_name = "사용자"
        verbose_name_plural = "사용자"
