from django.urls import path

from . import views

app_name = 'nps'
urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.submit_answer, name='submit_answer'),
    path('thanks/', views.thanks, name='thanks')
]