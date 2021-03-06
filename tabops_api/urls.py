"""tabops_api URL Configuration

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
# from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls
API_TITLE = 'API title'
API_DESCRIPTION = '...'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path(r'api/user/', include('users.urls')),
    path(r'api/bstype/', include('bstype.urls')),
    path(r'api/asset/', include('asset.urls')),
    path(r'api/architecture/', include('architecture.urls')),
    path(r'api/salt/', include('salt.urls')),
    path(r'api/zabbix/', include('zabbix.urls')),
    path(r'api/upload/', include('upload.urls')),
    path(r'api/docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
