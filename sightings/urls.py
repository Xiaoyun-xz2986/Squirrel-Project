from django.urls import path

from . import views

app_name = 'sightings'

urlpatterns = [
    path('', views.list_squirrels, name='list_squirrels'),
    path('<str:squirrel_id>/', views.edit_squirrels, name='edit'),
]
