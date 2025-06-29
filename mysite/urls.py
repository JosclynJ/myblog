"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static

from mysite.views import *
from mysite.authentication import *


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('artikels/<int:id>/', artikel_detail, name='artikel_detail'),
    path('dashboard', dashboard, name='dashboard'),
    path('dashboard/artikel-list', artikel_list, name='artikel_list'),

    path('dashboard/', include("artikels.urls")),

    ######## Authentication ########
    path('auth-login', login, name='login'),
    path('auth-logout', logout, name='logout'),
    path('auth-registrasi', registrasi, name='registrasi'),
]

############### Media ###############
# Menambahkan rute untuk file statis (hanya saat DEBUG=True)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Menambahkan rute untuk file media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Menambahkan rute untuk CKEditor
urlpatterns += [
    path("ckeditor5/", include('django_ckeditor_5.urls')),
]