from django.urls import path, include
from .views import FreelancerRegister, FreelancersDetails, FreelancerDetail

urlpatterns = [
    path('register/', FreelancerRegister.as_view(), name='register'),
    path('career/', FreelancersDetails.as_view(), name='career'),
    path('career/<int:pk>/', FreelancerDetail.as_view(), name='careerDetail')
]
