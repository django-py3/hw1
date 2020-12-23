from django.db import models

# Create your models here.
class Pages(models.Model):
    title = models.CharField(max_length=250)
    pagebody = models.TextField()
    author = models.ForeignKey(
        'auth.User', # дефолтынй пользователь из django.contrib.auth
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return self.title 