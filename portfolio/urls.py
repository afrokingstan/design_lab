from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_portfolio, name='portfolio'),
    #path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_portfolio, name='add_portfolio'),
    ]