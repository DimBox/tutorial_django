from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'change', views.change_color),
    url(r'$', views.home_page),
]
