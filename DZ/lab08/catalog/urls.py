from django.urls import path
from . import views

app_name = 'catalog'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:reg_id>/', views.detail, name='detail'),
]