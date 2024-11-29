from django.urls import path

from agro_marketplace.sellers import views

urlpatterns = [
    path('create/', views.create_seller, name='create_seller'),
    path('<int:pk>/', views.card_info_sellers, name='card_info_sell'),
]
