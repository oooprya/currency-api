from django.urls import path
from . import views

app_name = 'exchanger'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:exchanger_id>', views.single_exchanger, name='single_exchanger')
]
