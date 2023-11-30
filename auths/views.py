from django.db.models import Q
from rest_framework import generics , viewsets, permissions ,status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import CustomUserSerializer
from .permissions import IsStudent,IsTeacherOrAdmin
from rest_framework.exceptions import ValidationError

# class based view singnup for user user will be Teacher or Student
class SignupView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

# User Login view 
class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            # Getting the user with given credentials
            user = CustomUser.objects.get(Q(email=email) & (Q(user_type__in=['teacher', 'student']) | Q(is_superuser=True)))

            # Checking the password from the given credentials and the user credentials is same
            if user and user.check_password(password):
                # making the Custom
                refresh = RefreshToken.for_user(user)
                data = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
                return Response(data)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User does not exist '}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': 'Invalid request '}, status=status.HTTP_400_BAD_REQUEST)

# view set to all the HTTP methods
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_permissions(self):
        if self.action == 'retrieve':
            return [IsStudent()]
        else:
            return [IsTeacherOrAdmin()]
        
    #   manipulating inbuild retrieve
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Check if the current user is the owner of the instance or an admin or teacher
        if (instance == request.user) or (request.user.user_type == 'teacher') or request.user.is_superuser:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            raise ValidationError("You are not allowed to retrieve this user's data.")
    