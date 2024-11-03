from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseNotAllowed
from .models import Question, Answer
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    page = request.GET.get('page','1')
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list,10)
    page_obj = paginator.get_page(page)
    return render(request, "trade/question_list.html", {"question_list":page_obj})

def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'trade/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('trade:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form} 
    return render(request, 'trade/question_detail.html', context) #이거 form을 같이 보내주는게 post로 값 받을 때 form 태그에 값 없으면 html에서 오류문 띄울라고


def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('trade:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'trade/question_form.html', context)
