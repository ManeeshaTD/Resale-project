from django.urls import path
from . views import *

app_name = 'accounts'

urlpatterns = [
    path('register/' , register , name='register'), 
    path('login-user/' , login_user , name='login-user'), 
    # path('password_change/' , auth_views.PasswordChangeView.as_view() , name='password_change') ,
    # path('password_change/done/' , auth_views.PasswordChangeDoneView.as_view() , name='password_change_done') , 
    # path('password_reset/' , auth_views.PasswordResetView.as_view() , name='password_reset') , 
    # path('password_reset/done/' , auth_views.PasswordResetDoneView.as_view() , name='password_reset_done') ,
]