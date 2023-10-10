
from django.urls  import path
from . import views

app_name = 'newapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('author_add/', views.author_add, name='author_add'),
    path('quotes_add/', views.quotes_add, name='quotes_add'),
    path('author/', views.author, name='author'),
    path('quotes/', views.quotes, name='quotes'),
]

