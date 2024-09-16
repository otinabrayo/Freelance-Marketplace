from django.contrib.auth.models import User
from rest_framework import generics
from .models import Freelancers
from rest_framework.response import Response
from .Freelancer.serializers import FreelancerSerializer, FreelancerDetailSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

class FreelancerRegister(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = FreelancerSerializer
    permission_classes = [AllowAny]

class FreelancersDetails(generics.ListCreateAPIView):
    queryset = Freelancers.objects.all()
    serializer_class = FreelancerDetailSerializer


class FreelancerDetail(generics. RetrieveUpdateDestroyAPIView):
    queryset = Freelancers.objects.all()
    serializer_class = FreelancerDetailSerializer
