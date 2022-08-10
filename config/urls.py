from django.contrib import admin
from django.urls import path, include
from pybo.views import base_views

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # project app
    path('', base_views.index, name='index'),
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
]
