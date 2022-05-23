from django.http.response import HttpResponse
from rest_framework.decorators import action
from restapiapp.models import SlackMessage
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseServerError
from rest_framework import status
from django.utils import timezone
import json

class ResponseViewSet(ViewSet):

    def create(self, request):
        """
        creates a new history record in the database
        """
        new_message = SlackMessage()
        new_message.submission_date = request.data["goal_date"]
        new_message.goal_date = request.data["time_spent"]
        new_message.save()
        serializer = ResponseSerializer(
            new_message, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlackMessage
        fields = ('id', 'submission_date', 'goal_date')