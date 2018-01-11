from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import Http404

from .models import *



# #API DOCUMENTATION
#
# #API
# #/Api/lobby/<pk>
# class LobbyDetail(APIView):
#     def get_object(selfs,pk):
#         try:
#             return PersonalInformation.objects.get(pk=pk)
#         except PersonalInformation.DoesNotExist:
#             raise Http404
#     def get(self,request,pk,format=None):
#         student=self.get_object(pk)
#         serializer=StudentSerializer(student)
#         return Response(serializer.data)
#     def delete(self,request,pk,format=None):
#         student=self.get_object(pk)
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# #/Api/student/
# class LobbyList(APIView):
#     def get(self,request):
#         students = Lobby.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)
#     def post(self,request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
