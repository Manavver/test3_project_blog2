## app1 url page
from django.urls import path
from .import views
urlpatterns = [

    path('Actors/',views.Actor_list),
    path('Actor/<int:pk>/', views.Actor_details, name='actor_details'),
    path('Actor/<int:pk>/delete/', views.delete_actor, name='del_actor'),
]
