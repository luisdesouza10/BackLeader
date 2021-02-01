from django.urls import include, path
from . import views

urlpatterns = [
  path('getProducts', views.getProducts),
  path('addProduct', views.addProduct),
  path('updateProduct/<int:product_id>', views.updateProduct),
  path('deleteProduct/<int:product_id>', views.deleteProduct),
]