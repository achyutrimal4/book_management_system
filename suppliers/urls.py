from django.urls import path, re_path
from . import views
urlpatterns = [
   path('', views.dashboard, name='dashboard'),
   path('suppliers/', views.suppliers, name='suppliers'),
]
