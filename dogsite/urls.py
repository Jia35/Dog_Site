"""dogsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from django.conf.urls.static import static
from django.conf import settings

from stores.views import home, foster, mine, message, message_user, collection, setting, user_info, getGPS
from pages.views import about, login, logout, register, register_info, register_info_dog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    re_path(r'^$', about, name='about'),
    path('home/', home, name='home'),
    path('foster/', foster, name='foster'),
    path('mine/', mine, name='mine'),
    path('message/', message, name='message'),
    re_path(r'^message_user/([a-zA-Z0-9]*)/$', message_user, name='message_user'),
    path('setting/', setting, name='setting'),
    path('collection/', collection, name='collection'),
    re_path(r'^user_info/([a-zA-Z0-9]{1,150})/$', user_info, name='user_info'),

    path('accounts/login/', login, name='login'),
    path('accounts/logout/', logout, name='logout'),
    path('accounts/register/', register, name='register'),
    path('register_info/', register_info, name='register_info'),
    path('register_info_dog/', register_info_dog, name='register_info_dog'),

    path('getGPS/', getGPS),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
