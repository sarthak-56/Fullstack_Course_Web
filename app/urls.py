from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('main/',main,name='main'),
    path('home/',home,name='home'),
    path('django',django,name='django'),
    path('express',express,name='express'),
    path('laravel',laravel,name='laravel'),
    path('spring',spring,name='spring'),
    path('ruby',ruby,name='ruby'),
    path('backend',backend,name='backend'),
    path('frontend',frontend,name='frontend'),
    path('database',database,name='database'),
    path('react',react,name='react'),
    path('angular',angular,name='angular'),
    path('next',next,name='next'),
    path('html',html,name='html'),
    path('vue',vue,name='vue'),
    path('mongo',mongo,name='mongo'),
    path('sql',sql,name='sql'),
    path('psql',psql,name='psql'),
    path('mariadb',mariadb,name='mariadb'),
    path('redis',redis,name='redis'),
]


