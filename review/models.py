from django.db import models
from user.models import User
'''
class User(models.Model):
    userId = models.IntegerField(primary_key=True)
    userEmail = models.CharField(max_length=30)
    userPw = models.CharField(max_length=20)
    userName = models.CharField(max_length=20)

    def __int__(self):
        return self.userId
'''
class Review(models.Model):
    reviewId = models.IntegerField(primary_key=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    bookId = models.CharField(max_length=30)
    reviewTxt = models.TextField()

    def __int__(self):
        return self.reviewId
