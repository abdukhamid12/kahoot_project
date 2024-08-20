from django.db import models


class Category(models.Model):
    author = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='cat_logo/')
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='questions')
    logo = models.ImageField(upload_to='quiz_logo/')
    question = models.CharField(max_length=300)
    time = models.PositiveSmallIntegerField(default=10)

    def __str__(self):
        return self.question


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    answer = models.CharField(max_length=300)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer