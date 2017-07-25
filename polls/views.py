from django.http import HttpResponse
from django.template import loader


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
