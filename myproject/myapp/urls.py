from django.urls import path

from . import views

urlpatterns = [
    path('reviews/', views.ReviewListCreateAPIView.as_view(), name='review-list-create'),
    path('reviews/<uuid:uuid>/', views.ReviewRetrieveDeleteAPIView.as_view(), name='review-detail'),
    path('products/', views.ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', views.ProductRetrieveAPIView.as_view(), name='product-detail'),
]
