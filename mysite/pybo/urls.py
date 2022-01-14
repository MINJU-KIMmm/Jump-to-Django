from django.urls import path
from . import views

app_name='pybo'

urlpatterns = [
    path('', views.index, name='index'), #/pybo/ 는 index라는 URL 별칭
    path('<int:question_id>/', views.detail, name='detail'), #/pybo/2/는 detail 이라는 별칭 생김
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
]