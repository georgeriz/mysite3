from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render

from .models import Answer, AnswerForm, ExtraQuestion

from datetime import datetime


def index(request):
    answer_list = Answer.objects.all()
    return HttpResponse('<br/>'.join([str(a) for a in answer_list]))


def json_api(request):
    answer_list = Answer.objects.all()
    json_object = {'scores': [{'answer': a.answer_text, 'feedback': a.feedback_text} for a in answer_list]}
    return JsonResponse(json_object)


def submit_answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer_text = form.cleaned_data['answer_text']
            feedback_text = form.cleaned_data['feedback_text']
            answer_date = datetime.now()
            Answer(answer_text=answer_text, feedback_text=feedback_text, answer_date=answer_date).save()
            return HttpResponseRedirect('/nps/thanks/')
    else:
        form = AnswerForm()
        eq_list = ExtraQuestion.objects.filter(visibility=True)
    return render(request, 'nps/nps_form.html', {'form': form, 'eq_list': eq_list})


def thanks(request):
    return HttpResponse("thank you for answering!")
