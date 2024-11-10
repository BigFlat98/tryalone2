from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseNotAllowed
from .models import Question, Answer
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def trade_list(request):
    page = request.GET.get('page','1')
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list,10)
    page_obj = paginator.get_page(page)
    return render(request, "trade/question_list.html", {"question_list":page_obj})

def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'trade/question_detail.html', context)


@login_required(login_url='common:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('trade:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form} 
    return render(request, 'trade/question_detail.html', context) #이거 form을 같이 보내주는게 post로 값 받을 때 form 태그에 값 없으면 html에서 오류문 띄울라고


@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('trade:trade_list')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'trade/question_form.html', context)

@login_required(login_url='common:login')
def question_modify(request,question_id):
    question = get_object_or_404(Question,pk = question_id)
    if request.user != question.author :
        messages.error(request, '수정권한이 없습니다')
        return redirect('trade:detail',question_id = question.id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.mopdify_date = timezone.now()
            question.save()
            return redirect('trade:detail',question_id = question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'trade/question_form.html', context)

@login_required(login_url='common:login')
def question_delete(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('trade:detail',question_id = question.id)
    question.delete()
    return redirect('trade:trade_list')

@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('trade:detail', question_id=answer.question.id)
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('trade:detail', question_id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    context = {'form': form}
    return render(request, 'trade/answer_form.html', context)


@login_required(login_url='common:login')
def answer_delete(request,answer_id):
    answer = get_object_or_404(Answer,pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('trade:detail',question_id = answer.question.id)
    answer.delete()
    return redirect('trade:detail',question_id = answer.question.id)
