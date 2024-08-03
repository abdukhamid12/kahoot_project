from django.db import models

# Create your models here.
class Category(models.Model):
    author = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='cat_logo/')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='questions')
    logo = models.ImageField(upload_to='question_logo/')
    question = models.CharField(max_length=300)
    time = models.PositiveSmallIntegerField(default=10)

    def __str__(self):
        return self.question

class Option (models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer

