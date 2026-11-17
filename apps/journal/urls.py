from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GradeViewSet, LessonViewSet, kpi_view

router = DefaultRouter()
router.register(r'grades', GradeViewSet)
router.register(r'lessons', LessonViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('kpi/', kpi_view, name='kpi'),
]