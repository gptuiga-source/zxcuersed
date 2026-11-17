from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Avg
from .models import Grade, Lesson
from .serializers import GradeSerializer, LessonSerializer
from apps.catalog.models import Student

# API для просмотра оценок (только для авторизованных)
class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [IsAuthenticated]

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

# API для статистики (KPI)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def kpi_view(request):
    # Считаем средний балл по всем оценкам
    avg_grade = Grade.objects.aggregate(Avg('value'))['value__avg']
    total_grades = Grade.objects.count()
    
    return Response({
        "average_grade": round(avg_grade, 2) if avg_grade else 0,
        "total_grades": total_grades,
        "message": "Статистика успеваемости"
    })