from django.urls import path
from django.contrib.auth import views as auth_views
from common import views as common_views

app_name='common'

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='common/login.html'),name='login'),
    path('logout/', common_views.logout_view, name='logout'),
    path('signup/', common_views.signup, name='signup'),
]

