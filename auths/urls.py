from django.urls import path,include
from auths.views import UserLoginView,SignupView
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'officestaff', OfficeUserViewSet)

urlpatterns = [
    path('login/', UserLoginView.as_view()),
    path('register/', SignupView.as_view()),
    path('', include(router.urls)),
  
    
]