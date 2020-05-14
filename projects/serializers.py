from rest_framework import serializers
from .models import Application,Project
from accounts.models import Professor
from django.contrib.auth.models import User
from django.conf import settings
from accounts.serializers import UserSerializer,ProfessorSerializer


class ProjectSerializer(serializers.ModelSerializer):

    professor = ProfessorSerializer(read_only = True)

    class Meta:
        model = Project
        fields= '__all__'

    def create(self, validated_data):
        professor_data = validated_data.pop('professor')
        professor = Professor.objects.create(**validated_data)
        Project.objects.create(professor=professor, **professor_data)
        return professor



class ApplicationSerializer(serializers.ModelSerializer):

    project = ProjectSerializer(read_only = True)

    class Meta:
        model = Application
        fields = '__all__'
