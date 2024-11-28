

from django.urls import path

from Home import views

urlpatterns = [
    path('', views.Index_View, name='index'),
    # path('ComingSoon/', views.ComingSoon_View, name='ComingSoon')
]