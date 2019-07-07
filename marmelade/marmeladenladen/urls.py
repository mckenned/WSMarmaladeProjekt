from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from marmeladenladen.views import Recipe, SelectionView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('test/', views.fruitbasket, name='test'),
    path('sitenotice/', views.sitenotice, name='sitenotice'),
    path('recipe/', Recipe.as_view()),
    path('', views.index, name='index'),
    path('fruitbasket/', SelectionView.as_view(), name='fruitbasket'),
]
urlpatterns += staticfiles_urlpatterns()
