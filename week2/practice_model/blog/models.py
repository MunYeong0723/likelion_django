from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200) # 짧은 문자열
    pub_date = models.DateTimeField('date published')
    body = models.TextField() # 긴 문자열

    # 목록에서 게시글의 제목을 title로 보이도록 함
    def __str__(self):
        return self.title

    # 본문의 내용을 100글자까지만 보여주도록 하는 함수
    def summary(self):
        return self.body[:100]