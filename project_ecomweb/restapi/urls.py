from django.urls import path
from .views import CategoryApiView, ProductApiView, ProductApiIdView

urlpatterns = [
    path('category/', CategoryApiView.as_view(), name='category'),
    path('product/', ProductApiView.as_view(), name='product'),
    path('product/<int:id>/', ProductApiIdView.as_view(), name='product-by-id')
]