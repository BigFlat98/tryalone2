from django.contrib import admin
from .models import Question, Answer
# Register your models here.
class QuestionAdmin(admin.ModelAdmin): #admin 테이블 관리 페이지에 subject속성으로 검색하는 검색창 생성
    search_fields = ['subject']

class AnswerAdmin(admin.ModelAdmin): 
    search_fields = ['question']

admin.site.register(Question)
admin.site.register(Answer)