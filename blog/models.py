from django.db import models
from django.conf import settings

# Create your models here.
class Posting(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # ,related_name='postings' 
    

class Reply(models.Model):
    # id
    content = models.CharField(max_length=200)
    # Article 모델의 PK를 저장/Article 레코드 삭제 시 관련된 모든 Comment 레코드 삭제
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE)
    # FK의 경우 클래스 변수명 뒤에 _id가 자동으로 붙어서 테이블 column이 된다.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)