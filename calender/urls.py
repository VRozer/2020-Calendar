"""calender URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('jan/', include('jan.urls')),
    path('feb/', include('feb.urls')),
    path('mar/', include('mar.urls')),
    path('apr/', include('apr.urls')),
    path('may/', include('may.urls')),
    path('jun/', include('jun.urls')),
    path('jul/', include('jul.urls')),
    path('aug/', include('aug.urls')),
    path('sep/', include('sep.urls')),
    path('oct/', include('oct.urls')),
    path('nov/', include('nov.urls')),
    path('dec/', include('dec.urls')),
    path('months/', include('months.urls')),
]
