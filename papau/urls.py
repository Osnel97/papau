from django.urls import path
from papau import views


urlpatterns = [
     path('', views.index, name='index'),
    # path('add_car/', views.add_car, name='add_car'),

]