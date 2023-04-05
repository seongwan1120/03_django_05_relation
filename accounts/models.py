from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

from blog.models import Posting

class User(AbstractUser):
    # mbti = models.CharField(max_length=4)  # column 추가 시 default 세팅 필요.
    like_postings = models.ManyToManyField(Posting, related_name='like_users')  # 테이블 추가.

