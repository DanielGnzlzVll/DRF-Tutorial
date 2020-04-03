from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import parsers
from rest_framework import permissions

from . import models
from . import serializers

# Create your views here.

class TopicViewset(viewsets.ModelViewSet):
    """View to handle all topics    
    """
    permission_classes = []
    queryset = models.Topic.objects.all()
    serializer_class = serializers.TopicSerializer
    filterset_fields = "__all__"


class CourseViewset(viewsets.ModelViewSet):
    """View to handle courses, 
    a course can have documents!
    """
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    filterset_fields = "__all__"


class DocumentViewset(viewsets.ModelViewSet):
    """A super awesome file-api view
    s3, we go get you!! 
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Document.objects.all()
    serializer_class = serializers.DocumentSerializer
    filterset_fields = "__all__"
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
