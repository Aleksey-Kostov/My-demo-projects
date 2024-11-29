from django.urls import path

from agro_marketplace.buyers import views

urlpatterns = [
    path('create/', views.create_buyer, name='create-buyer'),
    path('<int:pk>/', views.card_info_buyer, name='card-info-buy'),
]
