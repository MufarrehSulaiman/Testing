from django.urls import path, include
from apps.bookmodule import views
urlpatterns = [
    path('',views.index,name='index'),
    path('name/',views.name,name='index')

]

