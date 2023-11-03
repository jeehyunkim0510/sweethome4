"""
URL configuration for sweethome4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from homeboardapp.views import start_work

urlpatterns = [
    path('', start_work,name='home'),
    path('admin/', admin.site.urls),
    path('homeboard/', include('homeboardapp.urls')),
    path('account/', include('accountapp.urls')),
    path('article/', include('articleapp.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
