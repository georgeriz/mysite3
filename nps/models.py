from django.db import models
from django.forms import ModelForm


class Answer(models.Model):
    choices = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10)]
    answer_text = models.IntegerField(choices=choices)
    user_text = models.CharField(max_length=200)
    feedback_text = models.CharField(max_length=200)
    answer_date = models.DateField()

    def __str__(self):
        return str(self.answer_text) + ', ' + self.feedback_text


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text', 'feedback_text']


class QnA(models.Model):
    question_text = models.CharField(max_length=200)
    # TODO the answer may not be text
    answer_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text
