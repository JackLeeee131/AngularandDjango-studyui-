"""mlyticsui URL Config

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.urls import include, path
from django.contrib import admin
from material.frontend import urls as frontend_urls
from studyui.admin import raw_admin_site

urlpatterns = [
    path('jet/',include('jet.urls', 'jet')),
    path('jet/dashboard/',include('jet.dashboard.urls', 'jet-dashboard')),
    # path('', include(frontend_urls)),
    # path('', include('studyui.urls')),
    # path('', admin.site.urls),
    path('dash/', admin.site.urls),
    path('admin/', raw_admin_site.urls),
    path('api/', include('mlytics_studio.api.urls')),
]
