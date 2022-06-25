from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author= models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body= models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    published_at= models.DateTimeField(blank=True, null=True)

    class Meta:
        pass

    '''return title as string representation of the model'''
    def __str__(self):
        return self.title

    '''set published date'''
    def publish(self):
        self.published_at= timezone.now()

    '''select approved comments'''
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("", {"pk":self.id})
        


class Comment(models.Model):
    author=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    post=models.ForeignKey(Post, related_name= "comments",on_delete=models.CASCADE)
    body=models.TextField()
    approved_comment= models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True)

    class Meta:
        pass


    '''return sectiopn of the text as string representation'''
    def __str__(self):
        return self.body[:10] + "..."

    def approve_comment(self):
        self.approve_comment=True
        self.save()

    def get_absolute_url(self):
        return reverse("", {"pk":self.post})

