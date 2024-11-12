from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from ..forms import QuestionForm
from ..models import Question
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
def question_vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    if request.user == question.author:
        messages.error(request, '자추 밴')
    else :
        question.voter.add(request.user)
    return redirect('trade:detail',question_id = question.id)