from django.db import models

class Post(models.Model):
    content1 = models.TextField()
    content2 = models.TextField()
    content3 = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content1