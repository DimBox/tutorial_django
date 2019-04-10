from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'home', views.home_page),
    url(r'$', views.home_page),
]
