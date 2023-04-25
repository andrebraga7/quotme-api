from django.urls import path
from quotes import views


urlpatterns = [
    path('quotes/', views.QuoteList.as_view()),
]
