from rest_framework import generics, permissions,status
from rest_framework.response import Response
from auths.serializers import  StudentSignupSerializer

# Create your views here.

class SignupView(generics.CreateAPIView):
    serializer_class = StudentSignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)