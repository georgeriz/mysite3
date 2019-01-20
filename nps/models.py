from django.db import models
from django.forms import ModelForm


class Answer(models.Model):
    answer_text = models.CharField(max_length=2)
    user_text = models.CharField(max_length=200)
    feedback_text = models.CharField(max_length=200)
    answer_date = models.DateField()

    def __str__(self):
        return self.answer_text + ', ' + self.feedback_text


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text', 'feedback_text']


class QnA(models.Model):
    question_text = models.CharField(max_length=200)
    answer_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text
