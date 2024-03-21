from django.urls import path,include
from .views import IndexView
from rest_framework.routers import DefaultRouter
from .views import ServerViewSet

router = DefaultRouter()
router.register('server',ServerViewSet,'server')

urlpatterns = [
    path('index/',IndexView.as_view(),name='index'),
    path('',include(router.urls)),
]