from django.urls import path,include
from auths.views import UserLoginView,StudentSignupView

urlpatterns = [
    
    path('login/', UserLoginView.as_view()),
    path('register/', StudentSignupView.as_view()),
    
  
    
]