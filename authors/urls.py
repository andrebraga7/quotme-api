from django.urls import path
from authors import views


urlpatterns = [
    path('authors/', views.AuthorList.as_view()),
]
