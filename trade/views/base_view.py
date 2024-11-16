from django.shortcuts import render, get_object_or_404
from ..models import Question
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def trade_list(request):
    page = request.GET.get('page','1')
    kw = request.GET.get('kw', '')
    question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
        Q(subject__icontains=kw) |  # 제목 검색
        Q(content__icontains=kw) |  # 질문 내용 검색
        Q(answer__content__icontains=kw) |  # 답변 내용 검색
        Q(author__username__icontains=kw) |  # 질문 작성자 검색
        Q(answer__author__username__icontains=kw)  # 답변 작성자 검색
    ).distinct()
    paginator = Paginator(question_list,10)
    page_obj = paginator.get_page(page)
    return render(request, "trade/question_list.html", {"question_list":page_obj,'page':page,'kw':kw})

def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'trade/question_detail.html', context)