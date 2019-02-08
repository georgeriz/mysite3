from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render

from .models import Answer, AnswerForm, ExtraQuestion, ExtraAnswer

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
        extra_question_list = request.POST.getlist('extra-question')
        extra_answer_list = [request.POST['extra-answer-{}'.format(q)] for q in extra_question_list]
        if form.is_valid():
            answer_text = form.cleaned_data['answer_text']
            feedback_text = form.cleaned_data['feedback_text']
            answer_date = datetime.now()
            answer = Answer(answer_text=answer_text, feedback_text=feedback_text, answer_date=answer_date)
            answer.save()
            eq_list = [ExtraQuestion.objects.filter(id=id) for id in extra_question_list]
            ea_list = [ExtraAnswer(extra_answer_text=t, answer=answer, extra_question=eq_list[i][0]) for i,t in enumerate(extra_answer_list)]
            map(lambda x: x.save(), ea_list)
            return HttpResponseRedirect('/nps/thanks/')
    else:
        form = AnswerForm()
        eq_list = ExtraQuestion.objects.filter(visibility=True)
    return render(request, 'nps/nps_form.html', {'form': form, 'eq_list': eq_list})


def thanks(request):
    return HttpResponse("thank you for answering!")
