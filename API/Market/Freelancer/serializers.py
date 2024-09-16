from django.contrib.auth.models import User
from ..models import Freelancers
from rest_framework import serializers

class FreelancerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class FreelancerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Freelancers
        fields = ['id', 'title', 'skill', 'bio', 'created_at', 'hour_rates']

