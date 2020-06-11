from django.shortcuts import render
from .models import *
# Create your views here.

def signUp(request):
    return render(request, 'home/sign-up.html')

def signIn(request):
    return render(request, "home/sign-in.html")

def home(request):
    return render(request,'home/home.html')

def myTest(request):
    return render(request,'home/my-test.html')

def doTest(request, exam_name):
    exam = Exam.objects.get(examName = exam_name)
    ques = list(Question.objects.filter(key = exam.id))
    ans = []
    for question in ques:
        ans.append(list(Answer.objects.filter(key = question.id)))
    # ans = list(Answer.objects.filter(key = ques[0].id))
    print(ans[0])
    return render(request,'home/do-test.html')