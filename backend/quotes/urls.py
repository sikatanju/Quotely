from django.urls import path
from . import views

urlpatterns = [
    path('', views.quotes_list),
    path('<int:id>', views.quotes_details),
    path('category/', views.category_list),
    path('category/<int:id>', views.category_details),
]