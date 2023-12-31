"""BaatCheet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('',views.WebPage,name='webpage'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    
    path('friends/',views.Frinds,name='friends'),
    path('groups/',views.Groups,name='groups'),
    path('anonymous/',views.Anonymous,name='anonymous'),
    path('ai_chat/',views.Ai_Chat,name='ai_chat'),
    path('vedio_chat/',views.Vedio_Chat,name='vedio_chat'),
    path('anonymous_chat/',views.Anonymous_Chat,name='anonymous_chat')

    
]



# Serve static files during development
if settings.DEBUG:
    print("-------------------------------")
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
