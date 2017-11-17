from django.shortcuts import render

# Create your views here.

def test(request):
    return render(request, 'y_plan.html')


def home(request):
    return render(request, 'home_base.html')

def news(request):
    return render(request, 'y_news.html')

def plan(request):
    return render(request, 'y_plan.html')

def peixun(request):
    return render(request, 'y_peixun_base.html')

def enterprise(request):
    return render(request, 'y_enterprise.html')

def recruitment(request):
    return render(request, 'y_recruitment.html')

