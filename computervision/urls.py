from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name = 'index'),
    #path('summarizer/', views.web_summarizer, name = 'summarizer'),
    #path('tweet_sentiments/', views.twitter, name='twitter'),
    #path('names/', views.name_classify, name='nigerian_names'),
]





