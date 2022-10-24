from django.db import models

class User(models.Model):
    name = models.TextField(default=False)
    gender = models.TextField()
    birth = models.DateField()
    # 오전이면 1, 오후면 +12시간 처리
    alarm = models.TimeField()
    # 1이면 로그인 된 상태, 디폴트는 0
    login = models.IntegerField(default=0)
    
