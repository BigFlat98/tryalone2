from django.shortcuts import render, get_object_or_404
from ..models import Question
from django.core.paginator import Paginator

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