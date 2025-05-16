from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    title = models.CharField( max_length = 100 )
    text = models.TextField( blank = True ) #blank=True 可以為空字串
    created = models.DateTimeField( auto_now_add = True ) #auto_now_add(建立時自動填上目前時間)
    date_completed = models.DateTimeField( null = True, blank = True ) #null=True(可以為空物件型態)
    important = models.BooleanField( default = False)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.id} - {self.title} - {self.created}"
    