from django.urls import path
from . import views
app_name = "embedContent"
urlpatterns = [
    path('' , views.home , name='home'),
    path('detail/<int:todo_id>/', views.detail, name='details'),
]