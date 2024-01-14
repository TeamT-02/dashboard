from django.contrib import admin
from django.urls import path, include
from . import user_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard', include('app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', user_login.REGISTER, name='register'),
    path('doLogin', user_login.DO_LOGIN, name='doLogin'),
    path('accounts/profile', user_login.PROFILE, name='profile'),
    path('accounts/profile/update', user_login.Profile_Update, name='profile_update'),
    path('logout/', user_login.logout_view, name='logout'),
    path('', include('main.urls'))
]
