from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from marmeladenladen.views import Recipe, SelectionView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('fruitbasket/', views.fruitbasket, name='fruitbasket'),
    path('recipe/', Recipe.as_view()),
    path('', views.index, name='index'),
    path('test/', SelectionView.as_view()),
]
urlpatterns += staticfiles_urlpatterns()
