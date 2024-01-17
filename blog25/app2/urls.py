from django.urls import path
from .import views
urlpatterns = [

    path('Actoress/',views.Actoress_list),
    path('Actoress/<int:pk>/', views.Actoress_details, name='actoress_details'),

]