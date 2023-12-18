"""
URL configuration for backend project.

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
from django.urls import path
from django.conf.urls import include
from filebrowser.sites import site
from rest_framework import routers
from rest_framework.authtoken import views
from lending_library.views import LoanViewSet
from lending_library.views import LocationViewSet
from lending_library.views import NetworkViewSet
from lending_library.views import LendableTypeViewSet
from lending_library.views import LendableStatusViewSet
from lending_library.views import LendableViewSet
from lending_library.views import LoanViewSet
from lending_library.views import UserViewSet
from lending_library.views import GroupViewSet, PermissionViewSet, ContentTypeViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'lendablestatus', LendableStatusViewSet)
router.register(r'loans', LoanViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'networks', NetworkViewSet)
router.register(r'lendabletypes', LendableTypeViewSet)
router.register(r'lendables', LendableViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'contenttype', ContentTypeViewSet)


urlpatterns = [
    path('admin/filebrowser/', site.urls),
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('admin/', admin.site.urls),

    path('', include(router.urls)),

    path('api-token-auth/', views.obtain_auth_token),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
