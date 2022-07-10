from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    avatar = models.ImageField(upload_to='avatar', default='user.png')

    def __str__(self):
        return self.user.username