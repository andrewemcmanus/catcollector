from django.urls import path
from . import views
# routes go here:
urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name='about')
]
