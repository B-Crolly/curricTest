from rest_framework import serializers
from .models import Survey


# serializer turns the python code from model into a JSON response
class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        #needs to match fields from model
        fields = ('id', 'code', 'name', 'exampleBoolean', 'answersRequired', 'created_at')
