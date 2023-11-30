from rest_framework import generics , viewsets, permissions
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import CustomUserSerializer
from .permissions import IsStudent,IsTeacherOrAdmin
from rest_framework.exceptions import ValidationError

class SignupView(generics.CreateAPIView):
    queryset = CustomUser.objects.filter(user_type='student')
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = CustomUser.objects.filter(email=email, user_type__in=['superadmin', 'teacher', 'student']).first()

        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(data)
        else:
            return Response({'error': 'Invalid credentials'}, status=401)
        
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_permissions(self):
        if self.action == 'retrieve':
            return [IsStudent()]
        else:
            return [IsTeacherOrAdmin()]
        
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Check if the current user is the owner of the instance or an admin or teacher
        if (instance == request.user) or (request.user.user_type == 'teacher') or request.user.is_superuser:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            raise ValidationError("You are not allowed to retrieve this user's data.")
    