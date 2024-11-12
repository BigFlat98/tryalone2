from django.contrib import admin
from django.urls import path, include
from trade import urls as trade_urls
from trade import views as trade_views
from .views import base_view ,question_view ,answer_view
app_name = 'trade'
urlpatterns = [
    path('',base_view.trade_list,name='trade_list' ),
    path('<int:question_id>/',base_view.detail,name='detail' ),
    path('answer/create/<int:question_id>/', answer_view.answer_create, name='answer_create'), 
    path('question/create/', question_view.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_view.question_modify, name='question_modify'), 
    path('question/delete/<int:question_id>/', question_view.question_delete, name='question_delete'), 
    path('answer/modify/<int:answer_id>/', answer_view.answer_modify, name='answer_modify'), 
    path('answer/delete/<int:answer_id>/', answer_view.answer_delete, name='answer_delete'), 
    path('question/vote/<int:question_id>/', question_view.question_vote, name='question_vote'), 
    path('answer/vote/<int:answer_id>/', answer_view.answer_vote, name='answer_vote'), 
]