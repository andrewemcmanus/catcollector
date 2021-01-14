from django.urls import path
from . import views
# routes go here:
urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name='about'),
    path('cats/', views.cats_index, name="cats_index"),
    path('cats/<int:cat_id>', views.cats_show, name='cats_show'),
    path('cats/create/', views.CatCreate.as_view(), name="cats_create"),
    path('cats/<int:pk>/update/', views.CatCreate.as_view(), name='cats_update'),
    path('cats/<int:pk>/delete/', views.CatCreate.as_view(), name="cats_delete"),
]
