from django.urls import path
from . import views
#djei349jdlsp
urlpatterns = [
    path('main/<str:firstname>', views.main, name='members'),
    path('registartion/', views.register, name='register'),
    path('testing/', views.testing, name='testing'),
    path('deletetask/<int:id>/<str:firstname>', views.deletetask, name='deletetask'),
]