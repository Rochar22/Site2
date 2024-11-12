from tempfile import template

from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from rest_framework.routers import DefaultRouter
from myblog.views import RegisterView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),  # Для главной страницы
    path('api/register/', RegisterView.as_view()),  # Маршрут для регистрации
]

urlpatterns += [
    path('', TemplateView.as_view(template_name='index.html')),
    re_path(r'^.*$', TemplateView.as_view(template_name='react_index.html'))
]