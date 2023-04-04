from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Comment(models.Model):
    # id
    content = models.CharField(max_length=200)
    # Article 모델의 PK를 저장/Article 레코드 삭제 시 관련된 모든 Comment 레코드 삭제
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # FK의 경우 클래스 변수명 뒤에 _id가 자동으로 붙어서 테이블 column이 된다.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

'''
article = Article.objects.create(title='월요일', content='싫어요')

c1 = Comment.objects.create(content='맞아', article_id=1)
c2 = Comment.objects.create(content='싫다', article_id=a1.id)  # DB 관점
c3 = Comment.objects.create(content='힘내', article=a1)  # 객체 관점

# c1 댓글이 달린 게시글: c1.article
# c1 댓글이 달린 게시글의 제목: c1.article.title

a1.comment_set
# a1에 달린 모든 댓글(모델명 소문자 + _set)
a1.comment_set.all()

# Comment 중에 article 항목이 a1인 모든 댓글(상동)
Comment.objects.filter(article=a1)

# a1에 달린 댓글을 pk 내림차순
a1.comment_set.order_by('-pk')
'''    