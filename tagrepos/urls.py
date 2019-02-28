from django.urls import path, re_path,include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name="index"),
    path('search', TemplateView.as_view(template_name='search.html'), name="search")
]