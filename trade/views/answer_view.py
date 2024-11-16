from django.shortcuts import render, redirect, get_object_or_404,resolve_url
from django.http import HttpResponseNotAllowed
from ..models import Question, Answer
from django.utils import timezone
from ..forms import  AnswerForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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
            return redirect('{}#answer_{}'.format(resolve_url('trade:detail',question_id = question.id),answer.id))
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form} 
    return render(request, 'trade/question_detail.html', context) #이거 form을 같이 보내주는게 post로 값 받을 때 form 태그에 값 없으면 html에서 오류문 띄울라고


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
            return redirect('{}#answer_{}'.format(resolve_url('trade:detail',question_id = answer.question.id),answer.id))
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

@login_required(login_url='common:login')
def answer_vote(request,answer_id):
    answer = get_object_or_404(Answer,pk=answer_id)
    if request.user == answer.author:
        messages.error(request,'자추 밴')
    else:
        answer.voter.add(request.user)
    return redirect('trade:detail',question_id = answer.question.id)

