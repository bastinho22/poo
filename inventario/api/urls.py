from rest_framework.routers import DefaultRouter
from inventario.api.views import productoviewset


router=DefaultRouter()
router.register('productos',productoviewset,basename='producto')
urlpatterns=router.urls