from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ProductViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
