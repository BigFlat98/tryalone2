from django.contrib import admin
from django.urls import path, include
from trade import urls as trade_urls
from trade import views as trade_views
app_name = 'trade'
urlpatterns = [
    path('',trade_views.trade_list,name='trade_list' ),
    path('<int:question_id>/',trade_views.detail,name='detail' ),
    path('answer/create/<int:question_id>/', trade_views.answer_create, name='answer_create'), 
    path('question/create/', trade_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', trade_views.question_modify, name='question_modify'), 
    path('question/delete/<int:question_id>/', trade_views.question_delete, name='question_delete'), 
    path('answer/modify/<int:answer_id>/', trade_views.answer_modify, name='answer_modify'), 
    path('answer/delete/<int:answer_id>/', trade_views.answer_delete, name='answer_delete'), 
]