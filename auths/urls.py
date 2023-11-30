from django.urls import path,include
from auths.views import UserLoginView,SignupView, CustomUserViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'user', CustomUserViewSet)

urlpatterns = [
    path('login/', UserLoginView.as_view()),
    path('register/', SignupView.as_view()),
    path('', include(router.urls)),
  
    
]