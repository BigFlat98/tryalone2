from django.contrib import admin
from django.urls import path, include
from trade import urls as trade_urls
from . import views
app_name = 'trade'
urlpatterns = [
    path('',views.index ),
    path('<int:question_id>/',views.detail,name='detail' ),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'), 
    path('question/create/', views.question_create, name='question_create'),
]