from django.urls import path
from . import views
urlpatterns = [
    path('', views.reg_user, name='reg_user')
]