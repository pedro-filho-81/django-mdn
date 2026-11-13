from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
# cria a classe questões
class Question(models.Model):
    # cria um campo para 200 caracteres
    question_text = models.CharField(max_length=200)
    # cria um campo para data e hora
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# cria a classe escolha
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text