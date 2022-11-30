from django.urls import path
from . import views
urlpatterns = [
    path('' , views.home),
    path('hello/' , views.say_hello),
    path('detail/<int:todo_id>/', views.detail, name='details'),
]