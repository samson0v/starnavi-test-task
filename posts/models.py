from django.db import models

from users.models import User


class Post(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    text = models.TextField(null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'#{self.pk} - {self.title} - {self.author}'


class Like(models.Model):
    who_like = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
