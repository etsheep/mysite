from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import render

from .models import Question


def index(request):
    template = loader.get_template('polls/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def login(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    if username == '逗比':
        return HttpResponse('恭喜逗比，登录成功！')
    return HttpResponse('登录失败！')


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
