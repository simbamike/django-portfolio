from django.urls import path, include
from portfolio import views

app_name="portfolio"

urlpatterns = [
    path('', views.index , name = 'index'),
    path('project/<int:pid>', views.project, name= 'project')
]
