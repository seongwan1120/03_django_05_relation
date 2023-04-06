from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # 회원가입 /accounts/signup/
    path('signup/', views.signup, name='signup'),
    
    # 로그인 /accounts/signin/
    path('signin/', views.signin, name='signin'),
    #로그아웃 /accounts/signout/
    path('signout/', views.signout, name='signout'),
    # 변수 처리 된 것이 아래에 와야 한다.
    # 프로필 /accounts/username/
    path('<str:username>/', views.profile, name='profile'),
    # 팔로우 /accounts/username/follow/
    path('<str:username>/follow', views.follow, name='follow'),
]   