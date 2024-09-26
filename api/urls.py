from django.urls import path

from .views import CartItemsViews

urlpatterns = [
    path('cart-items/', CartItemsViews.as_view(), name='cart-items'),
    path('cart-items/<int:pk>', CartItemsViews.as_view(), name='cart-items-detail'),
]