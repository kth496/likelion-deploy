from django.db import models

# Create your models here.

class Blog(models.Model): #하나의 블로그 기능
    title = models.CharField(max_length = 200) #제목은 200자 이상을 넘을 수 없음
    writer = models.CharField(max_length = 100)
    pub_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100] #글자 100자 이하 출력
