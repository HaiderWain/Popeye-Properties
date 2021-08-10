from django.urls import path
from . import views
from users import views as user_views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('search/', views.search, name='blog-request'),
    path('topsis/', views.topsisthebest, name='blog-topsis'),
    path('preferences/', views.displayprefrences, name='blog-preferences'),
    path('propertydetails/', views.displaypropertydetails, name='blog-propertydetails'),
    path('selectArea/', views.selectArea, name='blog-selectArea'),
    path('favorites/', views.favoriteProperties, name='favoriteProperties'),
    path('propertydetails/<int:pk>/', views.displaypropertydetails, name='blog-propertydetails'),
    path('logout/', views.logout_view, name='logout'),
]
