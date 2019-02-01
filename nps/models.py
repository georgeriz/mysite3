from django.db import models
from django.forms import ModelForm


class Answer(models.Model):
    choices = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)]
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


class ExtraQuestion(models.Model):
    extra_question_text = models.CharField(max_length=200)
    visibility = models.BooleanField()

    def __str__(self):
        return self.extra_question_text


class ExtraAnswer(models.Model):
    extra_question_id = models.ForeignKey(ExtraQuestion, on_delete=models.CASCADE)
    answer_id = models.ForeignKey(Answer, on_delete=models.CASCADE)
    extra_answer_text = models.CharField(max_length=200)
