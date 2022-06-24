from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from .models import (
    JobPostSkillSet,
    JobType,
    JobPost,
    Company
)
from django.db.models.query_utils import Q


class SkillView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        skills = self.request.query_params.getlist('skills', '')
        print("skills = ", end=""), print(skills)



        return Response(status=status.HTTP_200_OK)


class JobView(APIView):
    

    def post(self, request):
        print(request.data)
        job_type = (request.data.get("job_type", None))
        company_name = request.data.get("company_name", None)
        job_description = request.data.get("job_description", None)
        salary = request.data.get("salary", None)
        
        obj = JobType.objects.all()
        obj_dict = list(obj.values())
        
        types = []
        for i in obj_dict:
            types.append(i['job_type'])
        
        if job_type not in types:
            return Response({'error': 'job_type이 존재하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

        if company_name is None:
            obj = Company.objects.last()
            print(obj.id)
            company_name = obj.id + 1

            create_jobpost = JobPost.objects.create(
                job_type = JobType.objects.get(name=job_type),
                
                company_name = company_name,
                job_description = job_description,
                salary = salary
                )
            create_jobpost.save()

            return Response({'message': '임의의 회사 이름을 부여한 후 글이 등록되었습니다.'}, status=status.HTTP_200_OK)
        
        create_jobpost = JobPost.objects.create(
            job_type = job_type,
            company_name = company_name,
            job_description = job_description,
            salary = salary
            )
        create_jobpost.save()

        return Response({'message': '정상적으로 글이 등록되었습니다.'}, status=status.HTTP_200_OK)

