from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'change', views.change_color),
    url(r'home', views.home_page),
    url(r'', views.make_up),
]
