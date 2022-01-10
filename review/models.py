from django.db import models

class User(models.Model):
    userId = models.IntegerField(primary_key=True)
    userEmail = models.CharField(max_length=30)
    userPw = models.CharField(max_length=20)
    userName = models.CharField(max_length=20)

    def __int__(self):
        return self.userId

class Review(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    bookId = models.CharField(max_length=30)
    reviewId = models.IntegerField(primary_key=True)
    reviewTxt = models.TextField()

    def __int__(self):
        return self.reviewId