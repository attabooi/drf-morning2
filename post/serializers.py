from rest_framework import serializers
from .models import Company, JobPost, JobPostSkillSet, JobType



class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        fields = "__all__"

class JobPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JobPost
        fields = ['job_type','company_name','job_description','salary']

class JobPostSkillSetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JobPostSkillSet
        fields = "__all__"



