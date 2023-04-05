from django.urls import path
from .views import CategoryApiView, ProductApiView

urlpatterns = [
    path('category/', CategoryApiView.as_view(), name='category'),
    path('product/', ProductApiView.as_view(), name='product'),
]