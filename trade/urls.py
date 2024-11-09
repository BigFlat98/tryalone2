from django.contrib import admin
from django.urls import path, include
from trade import urls as trade_urls
from trade import views as trade_views
app_name = 'trade'
urlpatterns = [
    path('',trade_views.index,name='index' ),
    path('<int:question_id>/',trade_views.detail,name='detail' ),
    path('answer/create/<int:question_id>/', trade_views.answer_create, name='answer_create'), 
    path('question/create/', trade_views.question_create, name='question_create'),
]