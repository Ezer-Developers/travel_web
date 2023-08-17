from django.urls import path
from .views import normal_user_signup, other_user_signup,UserProfileUpdateView, UserProfileDetailView

urlpatterns = [
    path('normaluser/signup/', normal_user_signup, name='normaluser-signup'),
    path('otheruser/signup/', other_user_signup, name='otheruser-signup'),
    
    path('profile/update/', UserProfileUpdateView.as_view(), name='userprofile-update'),
    path('profile/', UserProfileDetailView.as_view(), name='userprofile-detail'),
]
