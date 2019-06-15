from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from marmeladenladen.views import MyView

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', MyView.as_view()),
    #path('generator', views.generator.as_view(), name='ingredients_list')
]
urlpatterns += staticfiles_urlpatterns()
